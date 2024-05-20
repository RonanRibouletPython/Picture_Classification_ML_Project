import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:

    def __init__(self,filename):
        self.filename = filename

    def predict(self):
        # Load the trained model
        model = load_model(os.path.join("artifacts","training", "model.keras"))
        # Load the test image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        # Transform the test image into an array
        test_image = image.img_to_array(test_image)
        # Expand the dimension of the test image
        test_image = np.expand_dims(test_image, axis = 0)
        # Predict the class of the test image
        result = np.argmax(model.predict(test_image), axis=1)
        # Print the predicted class of the test image
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
            return [{ "image" : prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{ "image" : prediction}]