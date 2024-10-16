#----------------------------------------
# Metashape helpers settings
# Code by S. Bär - April 2023
#----------------------------------------
# SETTINGS AND THEIR PURPOSE:
#   
#   SCRIPT SETTINGS:
#   ================
#   script_api_version  -> Used to check compatibility of the script with the installed Metashape version
#       
#   LOG SETTINGS:
#   ============
#   log_output_folder_path -> Path where the log files should be stored
#
#   DATASET STRUCTURE SETTINGS:
#   ==========================
#   use_folder_prefix   -> Used if you want to select datasets with a certain prefix only
#   folder_prefixes     -> Dataset prefixes that are accepted
#   model_folder_path   -> Location of the model folder (relative to dataset folder)
#   image_folder_path   -> Location of the image folder (relative to dataset folder)
#   image_extensions    -> Image types that are used eg. png, jpeg, etc.
#   cam_pos_file_path   -> Location of the cam position file (relative to dataset folder)
#   scan_info_file_path -> Location of the scan information file (relative to dataset folder)
#
#   SCAN INFORMATION REGEX SETTINGS:
#   ===============================
#   f_number_regex   -> Regex used to extract the f-number
#   num_images_regex -> Regex used to extract the number of needed images
#
#   INPUT OUTPUT FOLDER SETTINGS:
#   ============================
#   calculation_input_folder_path   -> Location of the 1_SCANNED folder (absolute path)
#   calculation_output_folder_path  -> Location of the 2_CALCULATED folder (absolute path)
#   export_input_folder_path        -> Location of the 3_UNPINNED folder (absolute path)
#   export_output_folder_path       -> Location of the 4_EXPORTED folder (absolute path)
#
#   # CALCULATION SETTINGS:
#   use_tweaks            -> Wether to use tweaks or not during the calculation. If you dont want to use tweaks just set it to False
#   tweaks                -> List of tweaks that are used to calculate the model. If you dont want to use tweaks just set use_tweaks to False
#   depthmap_downscale    -> Downscale factor of the depthmaps (0 = no downscale, 0 < = more down scaled)
#   use_smooth            -> Whether to smooth the calculated mesh or not
#   show_finished_message -> Whether to show a message after the calculation is done. If you don't want to show a message set this to False
#
#   EXPORT SETTINGS: 
#   ===============
#   image_texture_size -> Size of the exported texture (width and height are the same)
#
#----------------------------------------
class Settings:
    def __init__(self):
        self.settings = {
            # Script settings
            "script_api_version": "2.0",

            # Log settings
            "log_output_folder_path": "C:\\InsectScanner\\NoahSchluessel\\Test files",

            # Dataset structure settings
            "use_folder_prefix": False, 
            "folder_prefixes": ["ETHZ-ENT", "EXP"],
            "model_folder_path": "Model",
            "image_folder_path": "edof",
            "image_extensions": [".png", ".jpg", ".jpeg", ".tif", ".tiff"],
            "cam_pos_file_path": "CamPos.txt",
            "scan_info_file_path": "ScanInformation.pdf",

            # Scan info pdf regex
            "f_number_regex":   r"Camera Constant\/f \[px\]:([0-9]*.[0-9]*)",
            "num_images_regex": r"Num Images:([0-9]*)",
            
            # Helper input & output folders
            "calculation_input_folder_path":  "C:\\InsectScanner\\Data\\DataCurrent\\1_SCANNED\\1_PINNED",
            "calculation_output_folder_path": "C:\\InsectScanner\\Data\\DataCurrent\\2_CALCULATED",
            "export_input_folder_path":       "C:\\InsectScanner\\Data\\DataCurrent\\3_UNPINNED",
            "export_output_folder_path":      "C:\\InsectScanner\\Data\\DataCurrent\\4_EXPORTED",

            # Calculation settings
            "use_tweaks": False,
            "tweaks": [("ooc_surface_blow_up",  "0.75"), ("ooc_surface_blow_off", "0.75")],
            "depthmap_downscale": 0,
            "use_smooth": False,
            "show_finished_message": True,

            # Export settings
            "image_texture_size": 4096
        }
    
    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value

settings = Settings()