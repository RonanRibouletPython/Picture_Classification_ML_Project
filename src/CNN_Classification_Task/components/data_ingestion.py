import os
import urllib.request as request
import zipfile
from CNN_Classification_Task import logger
from CNN_Classification_Task.utils.common import get_size
from CNN_Classification_Task.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    # Downloads the file from the source URL and saves it to the local_data_file
    def download_file(self):
        # Check if the file already exists and download it
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            # Logs if the download was successful
            logger.info(f"{filename} is downloaded with the following infos: \n{headers}")
        else:
            # Logs if the file already exists
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  


    # Extracts the zip file into the data directory
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        # Check if the directory already exists and create it if not
        os.makedirs(unzip_path, exist_ok=True)
        # Extracts the zip file into the data directory
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

