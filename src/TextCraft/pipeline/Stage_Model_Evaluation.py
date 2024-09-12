from TextCraft.config.configuration import ConfigurationManager
from TextCraft.components.ModelEvaluation import ModelEvaluation
from TextCraft.logging import logger
import os
class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_eval_config()
        model_eval_config = ModelEvaluation(config = model_eval_config)

        metric_path = os.path.join("artifacts", "model_evaluation", "evaluation_results.csv")

        if os.path.exists(metric_path):
            print(f"Csv already exists at {metric_path}. Skipping ...")
        else:
            print("Csv not found. Starting evaluation...")
            model_eval_config.evaluate()