from TextCraft.config.configuration import ConfigurationManager
from TextCraft.components.DataIngestion import DataIngestion
from TextCraft.logging import logger

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    def main(self):

        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion_config = DataIngestion(config = data_ingestion_config)
        data_ingestion_config.download()
        data_ingestion_config.extract_zip_file()