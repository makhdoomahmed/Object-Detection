# Object Detection and Image Cropping Project
This project focuses on performing object detection using a pretrained YOLOv5s model. Following the detection, the script crops the original image based on the model's outputs, isolating the predicted objects. It will show the source image before the object detection and after the object detections. To run this project, you must setup your virtual environment.


## Usage
Run the main.py script to execute supporting scripts that perform object detection and create four folders:

- image_source folder: contain the source image
- runs folder: Contains labeled images with predicted bounding boxes.
- image_slice folder: Contains images of the predicted objects cropped from the original image.
- metadata folder: CSV file which contain the data and X,Y location of all dectected object from source image. 
  
## Paramaters accepted
- Testing with multiple paramaters
    - python main.py - with no paramater with default image
    - python main.py "image_source\Busy_Street.jpg" - with paramater for image location on local dirve
    - below is with image URL
    - python main.py https://upload.wikimedia.org/wikipedia/commons/0/09/The_smaller_British_birds_%288053836633%29.jpg
    
## Default image location
  - image_source\Busy_Street.jpg
    
## Predicted Sample location
- runs\detect\exp

## Cropped sample Location
- image_slice
