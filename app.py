from flask import Flask ,render_template ,request ,jsonify
import os
from flask_cors import CORS ,cross_origin
from cnnClassifierr.utils.common import decodeImage
from cnnClassifierr.pipeline.predict import PredictionPipeline

os.putenv('LANG' ,'en_US.UTF-8')
os.putenv('LC_ALL' ,'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(filename=self.filename)

@app.route('/' ,methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/train' ,methods=['GET' ,'POST'])
@cross_origin()
def trainRoute():
    os.system('dvc repro')
    return "Training Done Successfully!"

@app.route('/predict' ,methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image ,ClApp.filename)
    result = ClApp.classifier.predict()
    return jsonify(result)

if __name__=="__main__":
    ClApp = ClientApp()
    app.run(host='0.0.0.0' ,port=8080 ,debug=True)