from pypdf import PdfReader, PdfWriter
import glob

path = "test.pdf" # Path to the PDF file to split
name = "test" # The prefix of the output files.
files = glob.glob(path + "*.pdf")
cnt = 1

print(files)

for file in files:
    reader = PdfReader(file)
    for page in reader.pages:
        writer = PdfWriter()
        writer.add_page(page)
        with open(name + str(cnt) + ".pdf", 'wb') as fp:
            writer.write(fp)
        cnt += 1
