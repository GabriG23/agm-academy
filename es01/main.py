
import json
import sys
from fpdf import FPDF

def json_to_pdf(json_file, pdf_file):
    # Leggi il contenuto del file JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Crea un oggetto PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Scrive ogni riga del JSON nel PDF
    def write_line(key, value, indent=0):
        line = f"{'  ' * indent}{key}: {value}" if not isinstance(value, dict) else f"{'  ' * indent}{key}:"
        pdf.cell(0, 10, txt=line, ln=True)
        if isinstance(value, dict):
            for k, v in value.items():
                write_line(k, v, indent + 1)

    for key, value in data.items():
        write_line(key, value)

    # Salva il file PDF
    pdf.output(pdf_file)
    print(f"PDF creato: {pdf_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Scrivere: python json_to_pdf.py input.json output.pdf")
    else:
        json_to_pdf(sys.argv[1], sys.argv[2])