import pandas as pd
from PIL import Image 
import cv2
import time
from crop import object_crop
from model import model_prediction

#### Creating main function
def main(image_path,info_path):
    #### Passing Image and calling Object predition model
    outcome = model_prediction(image_path)
    #### showing the outcome of the process
    outcome.show(), outcome.save() 
    ####  DataFrame for different detected objects 
    df = outcome.pandas().xyxy[0]
    df.to_csv('metadata\metadata.csv', index = False)
    #### applying delay to compete the process
    time.sleep(7)
    ### storing the detected objects details from image in CSV
    object_crop(image_path, info_path)



if __name__ == "__main__":
    image_path = "image_source\Busy Street.jpg"
    info_path = "metadata\metadata.csv"
    main(image_path,info_path)