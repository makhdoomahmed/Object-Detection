import cv2
import torch

def model_prediction(image_path):

    print("****************Model Initilaizing ***************")
    #### calling pretained model yolov5
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s',_verbose=False)
    
    objimage = cv2.imread(image_path)
    objimage = cv2.cvtColor(objimage, cv2.COLOR_BGR2RGB)
    results = model(objimage)
    
    return results