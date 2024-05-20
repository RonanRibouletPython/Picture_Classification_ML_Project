# Import the log handler
from CNN_Classification_Task import logger
from CNN_Classification_Task.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNN_Classification_Task.pipeline.stage_02_base_model import PrepareBaseModelTrainingPipeline
from CNN_Classification_Task.pipeline.stage_03_model_training import ModelTrainingPipeline
# Data ingestion stage
STAGE_NAME = "Data Ingestion stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 

   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()

   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e

# Base model preparation stage
STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

# Model training stage
STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
