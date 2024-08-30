# Compress the redof images
from PIL import Image
import os, glob
from settings import *

def compress(project):
    images = glob.glob(os.path.join(project, "edof/*.png"))
    if not os.path.exists(os.path.join(project, jpeg_folder_name)):
        os.mkdir(os.path.join(project, jpeg_folder_name)) # Create folder if missing
    for image in images:
        img = Image.open(image)
        file_name =  os.path.basename(image).rstrip("png")
        img.save(project + jpeg_folder_name + file_name + "jpeg", quality=jpeg_quality)
        print(file_name)
