#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Brightness of the image

from PIL import Image, ImageEnhance
import os

def increase_brightness(input_folder, output_folder, brightness_factor):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all images in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Open the image
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Increase brightness
            enhancer = ImageEnhance.Brightness(img)
            brightened_img = enhancer.enhance(brightness_factor)

            # Save the brightened image to the output folder
            output_path = os.path.join(output_folder, 'brightened_' + filename)
            brightened_img.save(output_path)

if __name__ == "__main__":
    # Replace 'input_folder' with the path to your dataset
    input_folder = 'D:/UVA/SE FOR ML/Project/final data/lap0123_preprocessed_datasets/Training_datasets_YES'

    # Replace 'output_folder' with the desired output path
    output_folder = 'D:/UVA/SE FOR ML/Project/final data/lap0123_preprocessed_datasets/Brightened_data'

    # Set the brightness factor (1.0 means no change, values greater than 1.0 increase brightness)
    brightness_factor = 1.5  # You can adjust this value as needed

    increase_brightness(input_folder, output_folder, brightness_factor)


# In[ ]:


#flipping the image
from PIL import Image
import os

def flip_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all images in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Open the image
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Flip the image horizontally
            flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

            # Save the flipped image to the output folder
            output_path = os.path.join(output_folder, 'flipped_' + filename)
            flipped_img.save(output_path)

if __name__ == "__main__":
    # Replace 'input_folder' with the path to your dataset
    input_folder = 'D:/UVA/SE FOR ML/Project/final data/lap0123_preprocessed_datasets/Training_datasets_YES'
    
    # Replace 'output_folder' with the desired output path
    output_folder = 'D:/UVA/SE FOR ML/Project/final data/lap0123_preprocessed_datasets/Flipped_data'

    flip_images(input_folder, output_folder)


# In[ ]:


#for flipping anular velocity.
import pandas as pd

def flip_angular_velocity(csv_path, output_csv_path):
    # Read the CSV file
    data = pd.read_csv(csv_path)

    # Flip the 'angular_velocity' column
    data['steering_input'] = -data['steering_input']

    # Save the modified data to a new CSV file
    data.to_csv(output_csv_path, index=False)

if __name__ == "__main__":
    # Replace 'input.csv' with the path to your CSV file
    input_csv_path = 'D:/UVA/SE FOR ML/Project/final data/lap0123_preprocessed_datasets/data.csv'

    # Replace 'output.csv' with the desired output path
    output_csv_path = 'D:/UVA/SE FOR ML/Project/final data/lap0123_preprocessed_datasets/Flippeddata.csv'

    flip_angular_velocity(input_csv_path, output_csv_path)

