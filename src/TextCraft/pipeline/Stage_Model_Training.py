from TextCraft.config.configuration import ConfigurationManager
from TextCraft.components.ModelTraining import ModelTrainer
from TextCraft.logging import logger
import os
class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)

        model_path = os.path.join("artifacts", "model_trainer", "gpt2", "model.safetensors")  # or 'pytorch_model.bin'

        if os.path.exists(model_path):
            print(f"Model already exists at {model_path}. Skipping training...")
        else:
            print("Model not found. Starting training...")
            model_trainer_config.train()






