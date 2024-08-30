@echo off
:: Wing => activate tweak and different input folder
"C:\Users\localadmin\AppData\Local\Programs\Python\Python38\python.exe" scripts/calculate.py --use_tweaks "True" --show_finished_message "False" --calculation_input_folder_path "C:\\InsectScanner\\Data\DataCurrent\\1_SCANNED\\2_WINGS"
"C:\Users\localadmin\AppData\Local\Programs\Python\Python38\python.exe" scripts/calculate.py --use_tweaks "False" --show_finished_message "True"