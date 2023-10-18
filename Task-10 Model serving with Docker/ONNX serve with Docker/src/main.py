import os
import cv2
import time
import uvicorn
import numpy as np
import onnxruntime
from fastapi import FastAPI, File, UploadFile, Request
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


class AppConfig(BaseSettings):
    app_name: str = "Model Serving Demo"
    version: str = "0.1"


class ImageConfigs(BaseSettings):
    img_shape: tuple = (224, 224)


class IndexResponse(BaseModel):
    response: str = "Model Serving Demo"


class ClassifierResponse(BaseModel):
    result: str
    top_probability: str


class VersionResponse(BaseModel):
    app_name: str
    version: str


appconfig = AppConfig()
imageconfig = ImageConfigs()

app = FastAPI(title=appconfig.app_name,
              version=appconfig.version,
              description="A demo backend app for serving image classification model with FastApi.")



@app.get("/")
async def index():
    return {"response": appconfig.app_name}


@app.get("/version", response_model=VersionResponse)
def version():
    return {
        "app_name": appconfig.app_name,
        "version": appconfig.version
    }

# declare model path here
random_weighted_path = "model/effcientv2b2.onnx"
pretrain_weighted_path = "model/efficientv2b2_p.onnx"
random_weighted = onnxruntime.InferenceSession(random_weighted_path)
pretrain_weighted = onnxruntime.InferenceSession(pretrain_weighted_path)


def model_predict(img, ort_session):
    img = cv2.resize(img, imageconfig.img_shape)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    x = img.astype(np.float32) / 255.0
    x = np.expand_dims(x, axis=0)
    x = np.transpose(x, (0, 3, 1, 2))

    input_name = ort_session.get_inputs()[0].name
    output_name = ort_session.get_outputs()[0].name

    preds = ort_session.run([output_name], {input_name: x})
    return preds[0]


def predict(contents, model):
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    preds = model_predict(img, model)

    class_names = ["cat", "dog"]
    probabilities = np.exp(preds) / np.sum(np.exp(preds))

    class_probabilities = [
        {"class": class_names[i].capitalize(), "probability": "{:.3f}".format(probabilities[0][i])}
        for i in range(len(class_names))
    ]

    sorted_classes = sorted(class_probabilities, key=lambda x: x["probability"], reverse=True)
    top_probability = sorted_classes[0]["probability"]
    top_classes = [item["class"] for item in sorted_classes]

    response_data = {
        "result": top_classes[0],
        "top_probability": top_probability,
        "classes": class_probabilities
    }
    return response_data,


@app.post('/predict_pretrain', response_model=ClassifierResponse)
async def predict_pretrain(image: UploadFile = File(...)):
    contents = await image.read()
    output = predict(contents, pretrain_weighted)
    return JSONResponse(content=output)


@app.post('/predict_random', response_model=ClassifierResponse)
async def predict_random(image: UploadFile = File(...)):
    contents = await image.read()
    output = predict(contents, random_weighted)
    return JSONResponse(content=output)



