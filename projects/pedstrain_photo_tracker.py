
import os

image_path = "E:\photos\ped1.jpeg"

if os.path.exists(image_path):
    print(f"The file at path {image_path} exists.")
    try:
        with open(image_path, 'rb') as file:
            print("The file is accessible.")
    except Exception as e:
        print(f"Error: {e}")
else:
    print(f"The file at path {image_path} does not exist.")
