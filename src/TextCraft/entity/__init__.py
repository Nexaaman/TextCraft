from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngectionConfig:
    root_dir: Path
    source_URL: str
    local_path: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status: Path
    REQUIRED_FILES: list

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer: str
    model: str

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model: str
    tokenizer: str
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int
    optim: str
    lr_scheduler_type: str
    fp16:  bool
    bf16:  bool
    use_4bit: bool
    bnb_4bit_compute_dtype: str
    bnb_4bit_quant_type: str
    use_nested_quant: False
    lora_r: int
    lora_alpha: int
    lora_dropout: int

