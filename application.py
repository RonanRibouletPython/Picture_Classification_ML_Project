from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from CNN_Classification_Task.utils.common import decodeImage
from CNN_Classification_Task.pipeline.model_prediction import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    # Use the main.py file to train the model
    os.system("python .\main.py")
    # Use the dvc repro command to reproduce the dvc file
    #os.system("dvc repro")
    return "Training done successfully!"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    # Call the predict method of the PredictionPipeline class
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    # Create an instance of the ClientApp class
    clApp = ClientApp()
    # Run the Flask app
    app.run(host='0.0.0.0', port=8080) #local host
