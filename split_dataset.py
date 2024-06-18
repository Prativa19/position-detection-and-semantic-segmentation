import glob
import random
import os
from shutil import copyfile


images = glob.glob("images/*.png")

print(f'Total images: {len(images)}')


train_img_dir = "/home/prativa/Desktop/bb_box/train/images/"
train_lbl_dir = "/home/prativa/Desktop/bb_box/train/labels/"
test_img_dir = "/home/prativa/Desktop/bb_box/test/images/"
test_lbl_dir = "/home/prativa/Desktop/bb_box/test/labels/"


os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(train_lbl_dir, exist_ok=True)
os.makedirs(test_img_dir, exist_ok=True)
os.makedirs(test_lbl_dir, exist_ok=True)

for img in images:
    try:

        filename = os.path.basename(img)
        label = os.path.join("labels", filename[:-4] + ".txt")  # Adjusted for '.png' to '.txt'

        if not os.path.exists(label):
            print(f'Label file {label} does not exist for image {img}')
            continue

        if random.random() < 0.8:
            copyfile(img, os.path.join(train_img_dir, filename))
            copyfile(label, os.path.join(train_lbl_dir, os.path.basename(label)))
        else:
            copyfile(img, os.path.join(test_img_dir, filename))
            copyfile(label, os.path.join(test_lbl_dir, os.path.basename(label)))
    except Exception as e:
        print(f'Error: {e} for image {img}')
