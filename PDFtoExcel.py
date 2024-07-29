import pdfplumber
import pandas as pd

# Funkcja do ekstrakcji tabel z pliku PDF
def extract_tables_from_pdf(pdf_path):
    all_tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            print(f"Przetwarzanie strony {i + 1} z {len(pdf.pages)}")
            extracted_table = page.extract_table()
            if extracted_table:
                df = pd.DataFrame(extracted_table[1:], columns=extracted_table[0])
                all_tables.append(df)
    combined_df = pd.concat(all_tables, ignore_index=True)
    return combined_df

# Zapisz połączoną tabelę do pliku Excel
def save_table_to_excel(table, output_path):
    table.to_excel(output_path, index=False)

# Ścieżka do pliku PDF
pdf_path = r"1.PDF"
# Ścieżka do pliku Excel
output_path = "2.xlsx"

# Ekstrakcja tabel i zapis do pliku Excel
combined_table = extract_tables_from_pdf(pdf_path)
save_table_to_excel(combined_table, output_path)

print("Tabela została zapisana do pliku Excel.")
