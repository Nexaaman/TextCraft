from TextCraft.pipeline.Stage_Data_Ingestion import DataIngestionPipeline
from TextCraft.pipeline.Stage_Data_Validation import DataValidationPipeline
from TextCraft.pipeline.Stage_Data_Transformation import DataTransformationPipeline
from TextCraft.pipeline.Stage_Model_Training import ModelTrainerPipeline
from TextCraft.logging import logger
STAGE_NAME = "DATA INGESTION"

try:
    logger.info(f"********************{STAGE_NAME}********************")
    data_ingestion  = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"********************{STAGE_NAME} Completed Successfully!!********************")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "DATA Validation"

try:
    logger.info(f"********************{STAGE_NAME}********************")
    data_ingestion  = DataValidationPipeline()
    data_ingestion.main()
    logger.info(f"********************{STAGE_NAME} Completed Successfully!!********************")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation"

try:
    logger.info(f"********************{STAGE_NAME}********************")
    data_ingestion  = DataTransformationPipeline()
    data_ingestion.main()
    logger.info(f"********************{STAGE_NAME} Completed Successfully!!********************")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "ModelTraining"

try:
    logger.info(f"********************{STAGE_NAME}********************")
    data_ingestion  = ModelTrainerPipeline()
    data_ingestion.main()
    logger.info(f"********************{STAGE_NAME} Completed Successfully!!********************")

except Exception as e:
    logger.exception(e)
    raise e