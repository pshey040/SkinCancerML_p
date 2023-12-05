from flask import Flask,flash,jsonify,request,render_template,redirect,url_for
import PIL
import numpy as np
import os
import models as SC
from werkzeug.utils import secure_filename

app=Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def runhome():

	
	return render_template('home.html')

@app.route('/showresult', methods=["GET","POST"])
def show():
	pic=request.files["pic"]
	inputimg = PIL.Image.open(pic)
	inputimg=inputimg.resize((28,28))
	img = np.array(inputimg).reshape(-1,28,28,3)
	result=SC.model.predict(img)

	result=result.tolist()
	print(result)
	max_prob=max(result[0])
	class_ind=result[0].index(max_prob)
	print(class_ind)
	result=SC.classes[class_ind]


	if (class_ind==0):
		info="Actinic keratosis"
	elif (class_ind==1):
		info="Basal cell carcinoma"
	elif (class_ind==2):
		info="Benign lichenoid keratosis"
	elif (class_ind==3):
		info="Dermatofibromas"
	elif (class_ind==4):
		info="Melanocytic nevus"
	elif (class_ind==5):
		info="Pyogenic granulomas" 
	elif (class_ind==6):
		info="Melanoma"
	return render_template('reults.html',result=result, info=info)


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5000, debug=True)



# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from models import SampleModelParams
# import prediction as MLApi

# app = FastAPI()

# origins = [
#   "*",
# ]

# app.add_middleware(
#   CORSMiddleware,
#   allow_origins=origins,
#   allow_credentials=True,
#   allow_methods=["*"],
#   allow_headers=["*"],
# )

# @app.get("/")
# async def index():
#   return {
#     "condition": "OK",
#     "model_version": "0.1.0"
#   }

# @app.post("/predict")
# async def predict_route(payload : SampleModelParams):
#   # TODO: Change this based on your model parameters
#   result = MLApi.make_prediction(
#     gender=payload.gender,
#     age=payload.age,
#   )

#   if result:
#     response = {"prediction": "Positive"}
#   else:
#     response = {"prediction": "Negative"}
#   return response