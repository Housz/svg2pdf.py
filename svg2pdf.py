# Description: This script converts all SVG files in a directory to PDF files.
# Reference: https://stackoverflow.com/a/5835909

import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

def convert_svgs_to_pdfs(input_folder, output_folder):
    
    # create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".svg"):
            
            svg_path = os.path.join(input_folder, filename)
            pdf_filename = f"{os.path.splitext(filename)[0]}.pdf"
            pdf_path = os.path.join(output_folder, pdf_filename)

            # convert SVG to PDF
            drawing = svg2rlg(svg_path)

            # save the PDF
            renderPDF.drawToFile(drawing, pdf_path)
            print(f"Conversion complete: {svg_path} -> {pdf_path}")

# specify the input and output folders
input_folder = './'
output_folder = './pdfs'


convert_svgs_to_pdfs(input_folder, output_folder)