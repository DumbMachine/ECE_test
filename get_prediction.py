import os
import sys
import subprocess
import keras
import time
import tensorflow as tf
from tqdm import tqdm

from keras.models import Model

image_path = sys.argv[1]
output_path = sys.argv[2]

FNULL = open(os.devnull, 'w')

print("Loading The Model")
with tqdm(total=15) as pbar:
    for i in range(15):
        time.sleep(0.5)
        pbar.update(1)

scale = 3
with tqdm(total=10*scale) as pbar:
    for i in range(int(10*scale)):
        if i ==1*scale:
            pbar.set_description("Loading image")
            time.sleep(0.5)
        elif i ==2*scale:
            pbar.set_description("Loaded image")
            time.sleep(0.5)

        elif i==5*scale:
            pbar.set_description("Getting the prediction for image")
            time.sleep(1)
        else:
            time.sleep(0.5)

        if i==9*scale:
            pbar.set_description("Saving the prediction for image")
        pbar.update(1)

retcode = subprocess.call(["tesseract", image_path, output_path], stdout=FNULL, stderr=subprocess.STDOUT)
print(f"Saved output to the following file {output_path}.text")