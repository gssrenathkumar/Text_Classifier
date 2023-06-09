import os
import urllib.request as request
import zipfile
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logger
from textSummarizer.utils.common import  get_size


class DataIngestion:
    def __int__(self,config:DataIngestionConfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrive(
                url =self.config.source_URL,
                filename =self.config.local_data_file
            )
            logger.info(f"f{filename} download with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        """
        Zip File Path: str
        Extracts the zip file into the data directory
        Function return None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)


