import pandas as pd
from PIL import Image 
import cv2
import time
from crop import object_crop
from model import model_prediction
import urllib
import requests
from io import BytesIO
import sys
import os

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

def open_image_from_url_or_default(url=None, save_location="image_source"):
    try:
        if url:
            # Fetch the image from the URL provided
            response = requests.get(url, verify=False)
            # Check if the request was successful
            response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
            image = Image.open(BytesIO(response.content))
        else:
            # If no URL is provided, open the default image file
            image = Image.open("image_source\Busy_Street.jpg")
        
        # Save the image to the specified location
        if not os.path.exists(save_location):
            os.makedirs(save_location)
        image_save_path = os.path.join(save_location, 'downloaded_image.jpg')
        image.save(image_save_path)
        print(f"Image saved to {image_save_path}")

        return image
    except requests.exceptions.RequestException as e:
        #print(f"An error occurred while fetching the image from the provided URL: {e}") # to get details error message
        print(f"An error occurred while fetching the image from the provided URL:")
        raise e
    except FileNotFoundError:
        print("Error: The default image file does not exist.")
        raise e
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise e



if __name__ == "__main__":
    #image_path = "image_source\Busy Street.jpg"
        
    # Source: https://commons.wikimedia.org/wiki/File:The_Coleoptera_of_the_British_islands_(Plate_125)_(8592917784).jpg
    #"https://upload.wikimedia.org/wikipedia/commons/1/1b/The_Coleoptera_of_the_British_islands_%28Plate_125%29_%288592917784%29.jpg",
    # By Américo Toledano, Source: https://commons.wikimedia.org/wiki/File:Biblioteca_Maim%C3%B3nides,_Campus_Universitario_de_Rabanales_007.jpg
    #"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Biblioteca_Maim%C3%B3nides%2C_Campus_Universitario_de_Rabanales_007.jpg/1024px-Biblioteca_Maim%C3%B3nides%2C_Campus_Universitario_de_Rabanales_007.jpg",
    # Source: https://commons.wikimedia.org/wiki/File:The_smaller_British_birds_(8053836633).jpg
    #"https://upload.wikimedia.org/wikipedia/commons/0/09/The_smaller_British_birds_%288053836633%29.jpg"
    
    # resource = urllib.request.urlretrieve("https://www.tensorflow.org/static/hub/tutorials/object_detection_files/output_YLWNhjUY1mhg_1.png", "image_source\local-filename.png")
    #ssl._create_default_https_context = ssl._create_unverified_context
    
    #image_url= "https://upload.wikimedia.org/wikipedia/commons/1/1b/The_Coleoptera_of_the_British_islands_%28Plate_125%29_%288592917784%29.jpg"
    #image_url= sys.argv[1]
    # Check if a command line argument was provided

    if len(sys.argv) > 1:
        image_url = sys.argv[1] 
    else: 
        image_url = None
    
    #resource = urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/0/09/The_smaller_British_birds_%288053836633%29.jpg", "image_source\local-filename.jpg")
    #image_path = "image_source\local-filename.jpg"
    
    
    
    #urllib.request.urlopen("https://upload.wikimedia.org/wikipedia/commons/1/1b/The_Coleoptera_of_the_British_islands_%28Plate_125%29_%288592917784%29.jpg").read()
    try: 
        # Test the function with no URL to open the default image
        image_to_open = open_image_from_url_or_default(image_url)
        if image_to_open:
            image_to_open.show()  # This will open the image with the default image viewer on your computer
            image_path = "image_source\downloaded_image.jpg"
            info_path = "metadata\metadata.csv"
    
            main(image_path,info_path)
    except Exception as e:
        print(f"Execution stopped due to an exception: {e}")

    #plt.imshow(image_path)
    #open(image_path,"wb")
    #show(image_path)
    #output.write(resource.read())
    #output.close()
   