PDF Extractor

This program is used to extract relevant information from a PDF file, including text and tables, and save the extracted tables to an Excel file. It also allows interaction with OpenAI's GPT-3.5-turbo model to process the extracted text.

Requirements

Before running the program, ensure you have the following Python packages installed:

- pdfplumber
- pandas
- openpyxl
- openai

You can install these packages using pip:

pip install pdfplumber pandas openpyxl openai

Usage

Command-Line Arguments

- filename: The path to the PDF file from which information will be extracted.
- -t, --text: Extracts text from the PDF.
- -tb, --table: Extracts tables from the PDF.
- -o, --output: Specifies the output filename for the extracted tables (in Excel format).
- -p, --photo: Placeholder for extracting photos from the PDF (currently not implemented).

Example Command

python main.py example.pdf -tb -o output.xlsx

Debugging in VSCode

If you are using Visual Studio Code for debugging, you can use the following launch.json configuration:

{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File with Arguments",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": ["example.pdf", "-tb", "-o", "output.xlsx"]
        }
    ]
}

Functions

extract_text_from_pdf(filename)

Extracts text from the specified PDF file.

Parameters:
- filename (str): The path to the PDF file.

Returns:
- all_text (list of str): A list of extracted text from each page of the PDF.

extract_tables_from_pdf(filename)

Extracts tables from the specified PDF file.

Parameters:
- filename (str): The path to the PDF file.

Returns:
- all_tables (list): A list of extracted tables from each page of the PDF.

save_tables_to_excel(all_tables, output_filename)

Saves the extracted tables to an Excel file.

Parameters:
- all_tables (list): A list of tables to be saved.
- output_filename (str): The output Excel file name.

call_chatgpt(pdf_text, user_prompt)

Sends extracted text to OpenAI's GPT-3.5-turbo model and returns the response.

Parameters:
- pdf_text (str): The extracted text from the PDF.
- user_prompt (str): The user's prompt for GPT-3.5-turbo.

process_text_with_chatgpt(all_text)

Processes extracted text with OpenAI's GPT-3.5-turbo model based on user prompts.

Parameters:
- all_text (list of str): A list of extracted text from each page of the PDF.

main()

The main function that parses command-line arguments and performs the specified actions (extract text, extract tables, save tables to Excel).

License

This project is licensed under the MIT License - see the LICENSE file for details.