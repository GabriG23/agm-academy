
import json
import sys
from fpdf import FPDF

def json_to_pdf(json_file, pdf_file):
    # Leggi il contenuto del file JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)     # carica i dati

    pdf = FPDF()                    # crea un pdf object
    pdf.add_page()                  # aggiunge una pagina
    pdf.set_font("Arial", size=12)  # setta il font

    for key, value in data.items():
        pdf.cell(0, 10, txt=f"{key}: {value}", ln=True)

    pdf.output(pdf_file)
    print(f"PDF creato: {pdf_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Scrivere: python json_to_pdf.py input.json output.pdf")
    else:
        json_to_pdf(sys.argv[1], sys.argv[2])