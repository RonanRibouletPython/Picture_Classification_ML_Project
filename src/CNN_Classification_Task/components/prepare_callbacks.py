# This callback routine will be used during the training of the model
# That is why we don't need to create a pipeline ofr it nor update the main.py file

import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time

from CNN_Classification_Task.entity.config_entity import PrepareCallbacksConfig

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config
   
    @property
    # Create the tensorboard callbacks
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir = tb_running_log_dir)   

    @property
    # Create the checkpoint callbacks for the best epoch
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath = self.config.checkpoint_model_filepath,
            save_best_only = True
        )

    # Create the callbacks
    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]