# Object Detection Assignment-1 Quater-4 Sir Anees
This initiative is concentrated on executing object localization tasks by deploying a pre-initialized YOLOv5s neural network. Subsequent to the object localization process, the algorithm executes a cropping operation on the source imagery, utilizing the bounding box coordinates delineated by the model's inference to segregate the anticipated object instances


## Usage
Run the main.py script to execute supporting scripts that perform object detection and create two folders:

- runs folder: Labeled images with predicted object bounding boxes. With each run it will create automatially new folder.
- image_slice: Contains the part of the detected image.
- image_source: Where your main image source.
- metadata: Creating the meta data details.


## Sample image used 
Please check .\image_source\Busy Street.jpg

## Predicted Object Images
Please check .\runs\detect\exp2\image0.jpg

## Meta data 
Please check .\metadata folder file name metadata.csv
