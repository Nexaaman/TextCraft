from TextCraft.pipeline.Stage_Data_Ingestion import DataIngestionPipeline
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