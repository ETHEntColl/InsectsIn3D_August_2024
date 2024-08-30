# Load data from the import folder decimates the model
# recalculates texture, calculates jpeg version of edof
# moves folder to export folder. 

import glob
import shutil
import pathlib
import logging
from run_metashape import run_metashape
from compress import compress
from settings import *
import time

# Print some info
print(import_path, export_path, log_file)


# Set up logger
logger = logging.getLogger('decimate_export_batch')
logging.basicConfig(filename=log_file, encoding='utf-8', level=logging.INFO, filemode='a')

# Check if settings are sensible
check_paths()
check_values()

errors = 0

# Extract files
files = glob.glob(import_path+"*\\*\\*.psx")

logger.info("####################################")
logger.info("Starting processing " + str(len(files)) + " files")
start = time.time()
for i, file_name in enumerate(files):
	try:
		logger.info("File: " + str(i))
		# Extract project name
		name = file_name.rstrip('.psx')
		name = name.split('\\')[-1]
		logger.info(name + " loaded")

		# Decimate model, recalculate texture, add metallic/roughness using metashape/pygltflib
		run_metashape(file_name)
		logger.info(name + " exported")

		# Compress the png images to jpeg
		project = str(pathlib.Path(file_name).parents[1]) + "\\"
		logger.disabled = True
		compress(project)
		logger.disabled = False
		logger.info(name + " compressed")
		
		# Move files to 
		shutil.move(import_path + name, export_path + name)
		logger.info(name + " moved")
		errors = 0

	except Exception as err:
		logger.info("EXCEPTION!" + str(err))
		errors += 1
		if errors >= errors_until_stop:
			logger.info("STOPPING SCRIPT. TOO MANY CONSECUTIVE FAILURES")
			raise Exception("Stopping Execution. Too many consecutive errors")
		else:
			logger.info("Skipping " + name)
			errors += 1
			continue

elapsed = time.time() - start
logger.info("EXPORT FINISHED IN " + str(elapsed) + " SECONDS")
