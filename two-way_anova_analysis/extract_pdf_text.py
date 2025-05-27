import PyPDF2
import sys

# Usage: python extract_pdf_text.py <input_pdf> <output_txt>
def extract_text_from_pdf(pdf_path, txt_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        with open(txt_path, 'w', encoding='utf-8') as out:
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    out.write(text + '\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python extract_pdf_text.py <input_pdf> <output_txt>')
        sys.exit(1)
    extract_text_from_pdf(sys.argv[1], sys.argv[2])
    print('Extraction complete.')