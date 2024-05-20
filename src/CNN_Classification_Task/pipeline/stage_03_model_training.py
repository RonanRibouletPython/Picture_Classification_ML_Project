from CNN_Classification_Task.config.configuration import ConfigurationManager
from CNN_Classification_Task.components.prepare_callbacks import PrepareCallback
from CNN_Classification_Task.components.model_training import Training
from CNN_Classification_Task import logger



STAGE_NAME = "Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Create the configuration manager object
        config = ConfigurationManager()
        # Load the callbacks configuration
        prepare_callbacks_config = config.get_prepare_callback_config()
        # Configure the callbacks
        prepare_callbacks = PrepareCallback(config = prepare_callbacks_config)
        # Get the callbacks
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        # Load the training configuration
        training_config = config.get_training_config()
        # Create the training object
        training = Training(config = training_config)
        # Load the base model
        training.get_base_model()
        # Create the validation dataset
        training.train_valid_generator()
        # Train the model
        training.train(
            callback_list = callback_list
        )


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        