from TextCraft.entity import (DataIngectionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig)

from TextCraft.constants import *
from TextCraft.utils.common import read_yaml, create_directories


class ConfigurationManager:
    def __init__(self, config_path = CONFIG_FILE_PATH, params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngectionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngectionConfig(
            root_dir=config.root_dir,
            source_URL = config.source_URL,
            local_path = config.local_path,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config
    
    def get_dataValidation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        get_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            status= config.status,
            REQUIRED_FILES = config.REQUIRED_FILES
        )
        return get_validation_config

    def get_data_transformation(self) -> DataTransformationConfig:
        config = self.config.data_tranformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path= config.data_path,
            tokenizer= config.tokenizer,
            model= config.model
        )
        return data_transformation_config


    def get_model_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        train_params = self.params.TrainingArguments
        bnb_params = self.params.bnb_config
        peft_config = self.params.peft_config
        create_directories([config.root_dir])

        get_model_training_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            data_path= config.data_path,
            model= config.model,
            tokenizer=config.tokenizer,
            num_train_epochs= train_params.num_train_epochs,
            warmup_steps= train_params.warmup_steps,
            per_device_train_batch_size=train_params.per_device_train_batch_size,
            per_device_eval_batch_size= train_params.per_device_eval_batch_size,
            weight_decay= train_params.weight_decay,
            logging_steps= train_params.logging_steps,
            evaluation_strategy= train_params.evaluation_strategy,
            eval_steps= train_params.eval_steps,
            save_steps= train_params.save_steps,
            gradient_accumulation_steps= train_params.gradient_accumulation_steps,
            optim= train_params.optim,
            lr_scheduler_type= train_params.lr_scheduler_type,
            fp16=  train_params.fp16,
            bf16= train_params.bf16,
            use_4bit= bnb_params.use_4bit,
            bnb_4bit_compute_dtype = bnb_params.bnb_4bit_compute_dtype,
            bnb_4bit_quant_type  = bnb_params.bnb_4bit_quant_type,
            use_nested_quant= bnb_params.use_nested_quant,
            lora_r = peft_config.lora_r,
            lora_alpha= peft_config.lora_alpha,
            lora_dropout= peft_config.lora_dropout
        )
        return get_model_training_config
