import numpy as np 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self ,filename):
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join('artifacts' ,'training' ,'model.h5'))

        imagename = self.filename
        test_img = image.load_img(imagename ,target_size=(224 ,224))
        test_img = image.img_to_array(test_img)
        test_img = np.expand_dims(test_img ,axis=0)
        result = np.argmax(model.predict(test_img) ,axis=1)
        print(result)

        if result[0] == 1:
            prediction = "Healthy"
            return [{'image': prediction}]
        else:
            prediction = "Coccidiosis"
            return [{'image': prediction}]