# Description: This script converts all SVG files in a directory to PDF files.

import os
import cairosvg

def convert_svgs_to_pdfs(source_dir, output_dir):
    # Make sure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".svg"):
            svg_path = os.path.join(source_dir, filename)
            
            base_name = os.path.splitext(filename)[0]
            pdf_filename = f"{base_name}.pdf"
            pdf_path = os.path.join(output_dir, pdf_filename)

            try:
                # Convert
                cairosvg.svg2pdf(url=svg_path, write_to=pdf_path)
                print(f"[OK]：{filename} -> {pdf_path}")
            except Exception as e:
                print(f"[ERR] {filename}: {str(e)}")

if __name__ == "__main__":
    SOURCE_DIRECTORY = "./"  # Source folder path
    OUTPUT_DIRECTORY = "./pdfss"  # Destination folder path

    convert_svgs_to_pdfs(SOURCE_DIRECTORY, OUTPUT_DIRECTORY)