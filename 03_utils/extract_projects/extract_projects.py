
import glob

projects_path = "Z:\\01_SCANNED_AND_PROCESSED\\01 CALCULATE GLB\\"
output_file = "nml.txt"

projects = glob.glob(projects_path+"*\\")
projects = [project.split('\\')[-2] for project in projects]


with open(output_file, 'w') as file:
    for project in projects:
        if 'NML' in project:  # Example usage: Extract all 'NML' insects
            file.write(f"{project}\n")
