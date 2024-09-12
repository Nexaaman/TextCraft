from TextCraft.entity import ModelTrainerConfig
import os


from transformers import (GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    Trainer,
    logging)
from peft import LoraConfig, PeftModel
from trl import SFTTrainer

from datasets import load_dataset, load_from_disk
import torch



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        
        tokenizer = GPT2Tokenizer.from_pretrained(self.config.tokenizer)

        dataset_pt = load_from_disk(self.config.data_path)
        tokenized_train_dataset = dataset_pt["train"]
        tokenized_eval_dataset = dataset_pt["validation"]

        tokenized_train_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])
        tokenized_eval_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

        bnb_config = BitsAndBytesConfig(
            load_in_4bit = self.config.use_4bit,
            bnb_4bit_quant_type = self.config.bnb_4bit_quant_type,
            bnb_4bit_compute_dtype =self.config.bnb_4bit_compute_dtype,
            bnb_4bit_use_double_quant=self.config.use_nested_quant
        )
        model = GPT2LMHeadModel.from_pretrained(self.config.model, quantization_config=bnb_config).to(device)
        
        compute_type = getattr(torch, 'float16')
        if compute_type == torch.float16 and self.config.use_4bit:
            major, _ = torch.cuda.get_device_capability()
            if major >=8:
                print("=" * 80)
                print("Your GPU supports bfloat16: accelerate training with bf16=True")
                print("=" * 80)

        peft_config = LoraConfig(
            lora_alpha=self.config.lora_alpha,
            lora_dropout=self.config.lora_dropout,
            r=self.config.lora_r,
            bias="none",
            task_type="CAUSAL_LM",
        )
        
        
        trainer_args = TrainingArguments(
                output_dir=self.config.root_dir, num_train_epochs=self.config.num_train_epochs, warmup_steps=self.config.warmup_steps,
                per_device_train_batch_size=self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_train_batch_size,
                weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
                evaluation_strategy=self.config.evaluation_strategy, eval_steps=self.config.eval_steps, save_steps=1e6,
                gradient_accumulation_steps=self.config.gradient_accumulation_steps, optim = self.config.optim,
                lr_scheduler_type = self.config.lr_scheduler_type, fp16=self.config.fp16, bf16=self.config.bf16
        )

        trainer = SFTTrainer(
            model=model,
            args=trainer_args,
            peft_config=peft_config,
            train_dataset=tokenized_train_dataset,
            eval_dataset=tokenized_eval_dataset,
            tokenizer=tokenizer,
            packing=True
        )

        trainer.train()

        trainer.model.save_pretrained(os.path.join(self.config.root_dir,"gpt2"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))   

        base_model = GPT2LMHeadModel.from_pretrained(
            model=model,
            low_cpu_mem_usage=True,
            return_dict=True,
            torch_dtype=torch.float16
        )

        final_model = PeftModel.from_pretrained(base_model, os.path.join(self.config.root_dir,"gpt2"))
        final_model = final_model.merge_and_unload()
        final_model.save_pretrained(os.path.join(self.config.root_dir,"gpt2"))


        
