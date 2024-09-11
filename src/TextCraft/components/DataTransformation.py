import os
from TextCraft.logging import logger
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from datasets import load_dataset, load_from_disk
from TextCraft.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = GPT2Tokenizer.from_pretrained(config.tokenizer)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = GPT2LMHeadModel.from_pretrained(config.model)
        self.model.resize_token_embeddings(len(self.tokenizer))
    def convert_example_to_features(self, example):
        tokenized_data = self.tokenizer(example["text"], padding = "max_length", truncation = True, max_length = 1024)
        tokenized_data["labels"] = tokenized_data["input_ids"].copy()
        return tokenized_data
    
    def convert(self):
        dataset = load_from_disk(self.config.data_path)
        dataset_pt = dataset.map(self.convert_example_to_features, batched=True, remove_columns=["text"])
        dataset_pt.save_to_disk(os.path.join(self.config.root_dir, "Dataset"))
