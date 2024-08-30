from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import pymupdf
import glob
import pandas as pd
import os

df = pd.read_csv('data.csv')

projects = df['Number']

print(df.head(5))

input_pdf = "ScanInformation.pdf"
path = "Z:\\01_SCANNED_AND_PROCESSED\\02 FINAL\\04_MHNN 20240729\\"
log_file = "C:\\InsectScanner\\NoahSchluessel\\Test files\\MHNN_OUT_PDF.txt"

def open_pdf(input_pdf):
    doc = pymupdf.open(input_pdf)
    try:
        pdf_text = doc[0].get_text("text") + doc[1].get_text("text")
    except:
        pdf_text = doc[0].get_text("text")
    return pdf_text.split('\n')

def modify_pdf_text(magnifcation, constant_mm, constant_f, object_pixel_pitch, text):
    working_distance = text[14].split(": ")
    height = float(text[6].split(": ")[1])
    width = float(text[7].split(": ")[1])
    text[12] = "Calibration (modified)"
    text[13] = f"2.1. Magnification: {magnifcation}"
    # text[14] = f"{working_distance[0]}: ({working_distance[1]}) might be incorrect" 
    text[15] = f"2.3. Camera Constant [mm]: {constant_mm}"
    text[16] = f"2.4. Camera Constant/f [px]: {constant_f}"
    text[17] = f"2.5. Object Pixel Pitch [um]: {object_pixel_pitch}"
    text[19] = f"Height [mm]: {object_pixel_pitch * height / 1000 :.2f}"
    text[20] = f"Width [mm]: {object_pixel_pitch * width / 1000 :.2f}" 
    return text


# Create a PDF using reportlab
def create_pdf(text_array, filename, indent_lines=None, bold_lines=None, double_indent_lines=None, triple_indent_lines=None, skip_lines=None, indent_value=20):
    if indent_lines is None:
        indent_lines = []
    if bold_lines is None:
        bold_lines = []

    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Set starting position
    x = 50
    y = height - 50

    # Set line height
    line_height = 14

    for index, line in enumerate(text_array):
        if index + 1 in bold_lines:
            c.setFont("Helvetica-Bold", 12)  # Set font to bold
        else:
            c.setFont("Helvetica", 12)  # Set font to normal

        if index + 1 in indent_lines:
            c.drawString(x + indent_value, y, line)  # Indent specific lines
        elif index + 1 in double_indent_lines:
            c.drawString(x + 2*indent_value, y, line)
        elif index + 1 in triple_indent_lines:
            c.drawString(x + 3*indent_value, y, line)
        elif index + 1 in skip_lines:
            y += line_height
        else:
            y -= line_height
            c.drawString(x, y, line)

        y -= line_height

    c.save()


indent_lines=[3, 9, 14, 15, 16, 17, 18, 19, 23, 28, 33, 35, 46, 47, 48, 49, 50, 52] 
bold_lines=[1, 2, 13, 22, 45]
double_indent_lines = [4, 5, 6, 10, 11, 12, 20, 21, 24, 25, 26, 27, 29, 30, 31, 32, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44]
triple_indent_lines = [7, 8]
skip_lines = [51, 53]


for i, item in df.iterrows():
    project = item['Number']
    print(project)
    if item['check1'] and not item['check2'] and '7' in project:
        # Specify the filename
        pdf_filename = "ScanInformation.pdf"
        if not os.path.exists(path + str(project) + "//" + input_pdf):
            continue
        cleaned_pdf_text = open_pdf(input_pdf=path + str(project) + "//" + input_pdf)
        cleaned_pdf_text = modify_pdf_text(item[' Magnification'], 
                                        item['Camera_Constant_mm'], 
                                        item['Camera_Constant_px'], 
                                        item['Object_Pixel_Pitch'],
                                        cleaned_pdf_text)

        # Create the PDF with text array
        create_pdf(cleaned_pdf_text, pdf_filename, indent_lines=indent_lines, bold_lines=bold_lines, double_indent_lines=double_indent_lines, triple_indent_lines=triple_indent_lines, skip_lines=skip_lines)

        # Read the PDF with PyPDF2 (if further manipulation is needed)
        reader = PdfReader(pdf_filename)
        writer = PdfWriter()

        # Add all pages to the writer
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

        # Save the final PDF
        with open(path + str(project) + "//" + pdf_filename, "wb") as f:
            writer.write(f)
        with open(log_file, 'a') as log:
            log.write(f"{project}: PDF created and saved as {pdf_filename}\n")
    else:
        with open(log_file, 'a') as log:
            log.write(f"Skipping {project}\n")

