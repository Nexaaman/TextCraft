import os
import urllib.request as request
from TextCraft.logging import logger
from TextCraft.utils.common import get_size
import zipfile
from TextCraft.entity import DataIngectionConfig
from pathlib import Path
class DataIngestion:
    def __init__(self, config: DataIngectionConfig):
        self.config = config
    
    def download(self):
        if not os.path.exists(self.config.local_path):
            filename, headers = request.urlretrieve(
                url= self.config.source_URL,
                filename = self.config.local_path
            )
            logger.info(f"{filename} is Download! Sucessfully!")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_path))}")
        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file info into the data directory
        function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
