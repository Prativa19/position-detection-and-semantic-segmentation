import glob
import os

labels = glob.glob("/home/prativa/Desktop/bb_box/labels/*.jpg.txt")

for lab in labels:
    base_name, extension = os.path.splitext(os.path.basename(lab))  # Get the base filename without extension
    new_name = base_name.replace('.jpg', '')  + extension # Remove .jpg and .png extensions
    
    new_path = os.path.join(os.path.dirname(lab),new_name)

    os.rename(lab,new_path)

    print(f'Renamed:{lab} to {new_path}')

