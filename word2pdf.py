import os
import docx2pdf

# Path to the folder containing the word files
input_folder = 'word'

# Path to the folder where the PDF files should be saved
output_folder = 'pdfs'

# Iterate over all files in the input folder
for file in os.listdir(input_folder):
  # Check if the file is a Word file (ends with .doc or .docx)
  if file.endswith('.doc') or file.endswith('.docx'):
    # Construct the full path to the file
    input_path = os.path.join(input_folder, file)
    # Construct the full path to the output PDF file
    output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.pdf')
    # Convert the Word file to PDF using docx2pdf
    docx2pdf.convert(input_path, output_path)
