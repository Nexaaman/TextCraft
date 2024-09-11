import os
from TextCraft.logging import logger
from TextCraft.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config = DataValidationConfig):
        self.config = config

    def validation_validate(self) -> bool:
        try:
            validation_status = None
            files = os.listdir(os.path.join("artifacts", "data_ingestion", "Dataset"))
            print(files)
            for file in self.config.REQUIRED_FILES:
                if file not in files:
                    validation_status = False
                    with open(self.config.status, "w") as f:
                        f.write(f"Validation STATUS: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status, 'w') as f:
                        f.write(f"Validation STATUS: {validation_status}")
            return validation_status
        except Exception as e:
            raise e