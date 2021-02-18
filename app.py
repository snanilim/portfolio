from typing import List
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
import os
import numpy as np
# import cv2
import matplotlib.pyplot as plt 
import uvicorn
# from OCR import prep, fullocr_single



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

'''
class FaceRecogData(BaseModel):
    Image1: np.array
    Image2: np.array
'''

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})   

# @app.get('/')
# def index():
#     return {"message": "New development"}

@app.get("/home", response_class=HTMLResponse)
def start_page(request: Request):
    print("start_page")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/home/FaceRecognition", response_class=HTMLResponse)
def start_page(request: Request):
    print("start_page")
    return templates.TemplateResponse("faceRecognition_Intro.html", {"request": request})

@app.get("/home/OCR", response_class=HTMLResponse)
def start_page(request: Request):
    print("start_page")
    return templates.TemplateResponse("OCR_Intro.html", {"request": request})

@app.get("/About", response_class=HTMLResponse)
def start_page(request: Request):

    return templates.TemplateResponse("about.html", {"request": request})

@app.post("/files/")
def create_upload_files(files: List[UploadFile] = File(...)):
    #print("entered")
    #name = '/home/sheba/Documents/Web development with Fast API/' + files[0].filename
    #print(name)
    #print(files[0].content_type)
    #print(len(files))
    
    '''
    with open(name, "wb+") as file_object:
        file_object.write(files[0].file.read())
    '''
    image_bytes = files[0].file.read()
    #print(type(image_bytes))
    # image_decoded = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
    

    #print(type(image_decoded))
    #cv2.imwrite(name, image_decoded)
    return {"info": "ok"}

# @app.post("/OCR_Result/")
# def OCR_files(files: UploadFile = File(...), response_class=PlainTextResponse):
#     #name = '/home/sheba/Documents/Web development with Fast API/' + files.filename
#     #print(name)
#     #print(files.content_type)
#     #print(len(files))
    
#     '''
#     with open(name, "wb+") as file_object:
#         file_object.write(files[0].file.read())
#     '''
#     image_bytes = files.file.read()
#     #print(type(image_bytes))
#     image_decoded = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
#     #print(type(image_decoded))
#     #cv2.imwrite(name, image_decoded)
#     #b64_string = base64.b64encode(image_bytes)
#     image_prep = prep(image_decoded)
#     text = fullocr_single(image_prep)
#     return text
#     #return {"filenames": [file.filename for file in files]}
#     #return {"filenames": type(files)}

@app.get("uploadfiles/")
def image():
    return {"upload files status": "working"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
    