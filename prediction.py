# import required libraries

import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models
import warnings
import joblib
import requests
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

# Load your model
loaded_model = joblib.load(r"C:\Users\Parsa\Downloads\MLOpsTemplate-master\MLOpsTemplate-master\joblib_SC_Model.pkl")

def make_prediction(param1, x_test, *args, **kwargs):
  # TODO: Actual prediction logic goes here.
 # Fit the params to your model and make prediction
  param1 = "https://www.skincancer.org/wp-content/uploads/melanoma_5_Evolving_Now-340x240.png"
  image_url = param1
  response = requests.get(image_url)
  image = Image.open(BytesIO(response.content))
  image = image.resize((28, 28))
  img = np.array(image)

  plt.imshow(img)
  plt.axis('off')
  plt.show()
  img = x_test[1]
  img = np.array(image).reshape(-1, 28, 28, 3)
  result = model.predict(img)
  #print(result[0])
  result = result.tolist()
  max_prob = max(result[0])
  class_ind = result[0].index(max_prob)
  print(classes[class_ind])

  prediction = classes[class_ind] # TODO: Hard coded to true. Implement your logic
  return prediction
