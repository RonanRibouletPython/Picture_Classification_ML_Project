
from CNN_Classification_Task.components.data_ingestion import DataIngestion
from CNN_Classification_Task.config.configuration import ConfigurationManager
from CNN_Classification_Task import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    # Copy the instanciation of the DataIngestion class in the main
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

# Load the main
if __name__ == '__main__':

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    # Exception handler
    except Exception as e:
        logger.exception(e)
        raise e