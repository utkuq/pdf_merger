import os
from PyPDF2 import PdfMerger

# PDF Location
pdf_dir = "./Files"

# Get files as a list
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

# Create a PdfFileMerger object
merger = PdfMerger()

# Loop through the PDF files and add them to the merger object
for pdf in pdf_files:
    merger.append(open(os.path.join(pdf_dir, pdf), 'rb'))

# Write the merged PDF to a file
with open("merged.pdf", "wb") as output:
    merger.write(output)
