import glob
import os
import logging
from tqdm import tqdm

path = "Z:\\01_SCANNED_AND_PROCESSED\\02 FINAL\\04_MHNN 20240729\\" # Path containing projects
log_file = "log.txt"

# Set up logger
logger = logging.getLogger('FINAL_CHECK')
logging.basicConfig(filename=log_file, encoding='utf-8', level=logging.INFO, filemode='w')

# Generate all project paths
projects = glob.glob(path + "*\\")

# Function to check structure.
def check_structure(path, files, folders):
    for file in files:
        found = False
        for x in file:
            if os.path.isfile(path + x):
                found = True
        if not found:
            logger.info(path + ": " + file[0] + " not found. (FILE)")
            return False
    
    for folder in folders:
        found = False
        for x in folder:
            if os.path.exists(path + x):
                found = True
        if not found:
            logger.info(path + ": " + folder[0] + " not found. (FOLDER)")
            return False
    return True

# Count number of files n. Returns True if min <= n <= max, False else.
def count(path, min, max):
    count = len(glob.glob(path + "*"))
    if min <= count <= max:
        return True
    logger.info(path + ": Too many or not enough files: " + str(count))
    return False

# Check the top folder of the project
def check_top_level(project, min, max):
    files = [['CamPos.txt'], ['cameras.xml'], ['ScanInformation.pdf', 'ParamsText.txt']]
    folders = [['Model'], ['edof'], ['redof']]
    return check_structure(project, files, folders) and count(project, min, max)

# Check the model folder of the project
def check_model(project, name, min, max):
    files = [[name + ".glb"], [name + ".psx"], [name + ".png"], [name + ".obj"], [name + '.mtl']]
    folders = [[name + '.files']]
    return check_structure(project + "Model\\", files, folders) and count(project + "Model\\", min, max)

# Compares redof and edof folder
def check_edof(project, min, max):
    edof = len(glob.glob(project + 'edof\\' + '*.png'))
    redof = len(glob.glob(project + 'redof\\' + '*.jpeg'))
    if min <= edof <= max and edof == redof:
        return True
    return False

for project in tqdm(projects):
    name = project.split('\\')[-2]
    check_top_level(project, 6, 8)
    check_model(project, name, 6, 7)
    check_edof(project, 350, 450)
    