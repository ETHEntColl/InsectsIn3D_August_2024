import glob
import shutil

path = "Z:\\01_SCANNED_AND_PROCESSED\\02 FINAL\\04_MHNN 20240729\\" # Root folder
old_name = "ScanInformation.pdf" # Current name of the document
new_name = "ScanInformationOld.pdf" # The name the copy of the document should have
projects = glob.glob(path + "*\\") # Make sure the glob settings are correct and the relevant file can be found

for project in projects:
    try:
        shutil.copy(project + old_name, project + new_name)
    except:
        # If there is no old_name or some other error occurs we skip the file.
        print("Skipping " + project)


