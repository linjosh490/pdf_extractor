import pdfplumber

def extract(filename):
    all_text = []
    all_tables = []

    with pdfplumber.open(filename) as pdf:
        # iterate over each page
        for page in pdf.pages:
            # extract text
            text = page.extract_text()
            all_text.append(text)
            table = page.extract_tables()
            all_tables.extend(table)

    return all_text, all_tables

def main():
    filename = "example.pdf"
    text, tables = extract(filename)
    extract("example.pdf")
    with open("extracted_text.txt", "w") as text_file:
        for page_text in text:
            text_file.write(page_text + "\n")

if __name__ == "__main__":
    main()
    