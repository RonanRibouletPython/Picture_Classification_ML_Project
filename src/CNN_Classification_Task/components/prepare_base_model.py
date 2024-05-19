

from pathlib import Path
from CNN_Classification_Task.entity.config_entity import PrepareBaseModelConfig
import tensorflow as tf

class PrepareBaseModel:
    # Initialize the configuration
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    # Get the VGG16 base model
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape = self.config.params_image_size,
            weights = self.config.params_weights,
            include_top = self.config.params_include_top
        )
        # Save the base model
        self.save_model(path = self.config.base_model_path, model = self.model)

    # A static method doesn't receive any reference argument 
    #whether it is called by an instance of a class or by the class itself
    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        # Freeze all the layers
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        # Freeze the layers till the freeze_till layer
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        # Flatten the output of the base model
        flatten_in = tf.keras.layers.Flatten()(model.output)
        # Add a dense layer with softmax activation
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)
        # Create the full model with the base model as input and the prediction as output
        full_model = tf.keras.models.Model(
            inputs = model.input,
            outputs = prediction
        )
        # Compile the full model
        full_model.compile(
            # optimizer = Stochastic Gradient Descent with the customed lr
            optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate),
            # loss = Categorical Crossentropy
            loss=tf.keras.losses.CategoricalCrossentropy(),
            # metrics = Accuracy
            metrics=["accuracy"]
        )
        # Print the summary of the full model
        full_model.summary()

        return full_model
    

    def update_base_model(self):
        # Update the base model
        self.full_model = self._prepare_full_model(
            model = self.model,
            classes = self.config.params_classes,
            freeze_all = True,
            freeze_till = None,
            learning_rate = self.config.params_learning_rate
        )
        # Save the updated base model
        self.save_model(path = self.config.updated_base_model_path, model = self.full_model)

    
    @staticmethod
    # Save the model
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)