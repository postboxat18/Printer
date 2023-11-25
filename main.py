import subprocess
import sys
import fitz
import os


def pdf_printer_page(pdf_file, printer_name):
    try:
        doc = fitz.open(pdf_file)
        for page_num in range(doc.page_count):
            output_path = os.path.join('File', f'page_{page_num + 1}.pdf')
            new_doc = fitz.open()
            new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
            new_doc.save(output_path)
            new_doc.close()
            if sys.platform.startswith('win'):
                subprocess.run(['print', '/D:', printer_name, output_path], check=True)
            elif sys.platform.startswith('linux'):
                subprocess.run(['lp', '-d', printer_name, output_path], check=True)
            else:
                print("Unsupported operating system")
    except Exception as e:
        print(f"Failed => {e}")


if __name__ == "__main__":
    pdf_file = "sample.pdf"
    printer_name = 'PRINTER_NAME'
    pdf_printer_page(pdf_file, printer_name)
