import pandas as pd
import cv2

def object_crop(image_path, info_path):
    # Read the image
    
    objimage = cv2.imread(image_path)
    df = pd.read_csv(info_path)
    # Iterate over rows in the DataFrame
    for index, row in df.iterrows():
        xmin, ymin, xmax, ymax = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
        class_name = row['name']

        # Crop the object from the image
        cropped_object = objimage[ymin:ymax, xmin:xmax]
        
        # Save or process the cropped object as needed
        cv2.imwrite(f'image_slice/{class_name}_{index}.png', cropped_object)
        