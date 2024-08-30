############################################################################################
# Settings
import_path = "Z:\\01_SCANNED_AND_PROCESSED\\01 CALCULATE GLB\\" # Where the projects are currently located
export_path = "Z:\\01_SCANNED_AND_PROCESSED\\02 FINAL\\" # Where the projects should be after the script finishes
log_file =  "Z:\\01_SCANNED_AND_PROCESSED\\01 CALCULATE GLB\\log.txt" # Where the log file is located

jpeg_folder_name = "redof\\" # Name of the folder that should be filled with the compressed images
jpeg_quality = 80  # The quality of the jpeg file.

max_face = 1000000 # The maximal amount of faces the resulting object should have
metallic = 0.02 # The metallic factor for the gltf material model
roughness = 0.1 # The roughness factor for the gltf material model

errors_until_stop = 2 # Number of consecutive errors needed to stop script. TODO: Maybe replace with overall failure?
############################################################################################

# Checks to test settings
import os

# Code is not clean. Sometimes string concat used for paths => necessary to have \\ at the end
def check_paths():
    if not os.path.exists(import_path):
        raise Exception("Your import path does not exist!")
    if not os.path.exists(export_path):
        raise Exception("Your export path does not exist!")
    if not import_path[-1] == "\\" or not export_path[-1] == "\\":
        raise Exception("Make sure your paths end on \\")

# To avoid having to run it again if misinput happens.
def check_values():
    if metallic > 0.2:
        x = input("Your metallic value(" + metallic + ") is high. Are you sure you want to continue? (y|N): ")
        if x.lower() != 'y':
            raise Exception("Change your metallic setting!")
    
    if metallic > 1 or roughness > 1:
        raise Exception("Metallic or roughness > 1!")
