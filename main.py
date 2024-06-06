import pdfplumber
import argparse
from openai import OpenAI

def extract_text_from_pdf(filename):
    all_text = []
    all_tables = []

    with pdfplumber.open(filename) as pdf:
        # iterate over each page
        for page in pdf.pages:
            # extract text
            text = page.extract_text()
            all_text.append(text)
            # table = page.extract_tables()
            # all_tables.extend(table)

    return all_text

def call_chatgpt(pdf_text, user_prompt): 
    client = OpenAI()
    content = f"{pdf_text}\n\n{user_prompt}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user", 
            "content": content,
            }
        ]
    )
    print(response.choices[0].message.content.strip())
    

def process_text_with_chatgpt(all_text): 
    combined_text = "\n".join(all_text)

    while True: 
        user_prompt = input("Enter your prompt (or type 'quit' to exit): ")
        if user_prompt.lower() == 'quit': 
            break 

        response = call_chatgpt(combined_text, user_prompt) 
        print("Response: ", response)



def main():
    parser = argparse.ArgumentParser(
        prog="pdf_extractor", 
        description="This program is used to extract relevant information from a PDF"        
    )

    parser.add_argument("filename")
    parser.add_argument("-t", "-text", action="store_true") # extracts text from PDF
    parser.add_argument("-p", "-photo", action="store_true") # extracts photos from PDF 
    parser.add_argument("-tb", "-table", action="store_true") # extracts tables from PDF 

    args = parser.parse_args() 
    filename = args.filename
    text = args.t
    table = args.tb
    photo = args.p

    if text:
        all_text = extract_text_from_pdf(filename)
        process_text_with_chatgpt(all_text)
    
    if table: 
        pass

    if photo:
        pass 

if __name__ == "__main__":
    main()
    