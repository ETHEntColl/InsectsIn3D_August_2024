from PyPDF2 import PdfReader
import glob
import pandas as pd

projects_path = "Z:\\01_SCANNED_AND_PROCESSED\\02 FINAL\\02_NML_20240826\\Check\\"
output_path = "pdf_values.csv"

projects = glob.glob(projects_path+"*\\")
project_names = [project.split('\\')[-2] for project in projects]
print(project_names)

def extract(list, prefix, sep=": "):
    for i, item in enumerate(list):
        if item.startswith(prefix):
            if item.split(sep)[1] == '':
                return list[i+1]
            return item.split(sep)[1]

def add(project_name, pdf, df, prefixes):
    row = [project_name]
    for prefix in prefixes:
        row.append(extract(pdf, prefix))
    
    df.loc[len(df.index)] = row  + ['']
    return df

if __name__ == '__main__':
    prefixes = ['2.1.', '2.3.', '2.4.', '2.5.', '2.2.']
    cols = ['Name', 'Magnification', 'Camera Constant [mm]', 'Camera Constant/f [px]', 'Object Pixel Pitch [um]', 'Working Distance [mm]', 'note']
    
    df = pd.DataFrame(columns=cols)
    for project, name in zip(projects, project_names):
        print(project)
        try:
            with open(project + "ScanInformation.pdf", "rb") as pdf_file:
                pdf_reader = PdfReader(pdf_file)
                pdf_text = pdf_reader.pages[0].extract_text()
        except Exception as err:
            df.loc[len(df.index)] = [name, 0, 0, 0, 0, 0, 'No ScanInformation.pdf']
            continue
        cleaned_pdf_text = pdf_text.split('\n')
        print(name)
        df = add(name, cleaned_pdf_text, df, prefixes)
        df.to_csv(output_path)
