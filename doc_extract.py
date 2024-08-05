import requests
from bs4 import BeautifulSoup

#target_url = "https://www.landonhotel.com"
target_url = "https://www.theleela.com/"

response = requests.get(target_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    text = ""
    for paragraph in soup.find_all('p'):
        text += paragraph.get_text()
        
    with open('website_text.txt', 'w') as text_file:
        text_file.write(text)
    
    print("Text extracted and saved successfully!")
    
    
""" ##using pdf file     
    
def extract_text_from_pdf(pdf_file_path):
    try:
        doc = fitz.open(pdf_file_path)
        pdf_text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            pdf_text += page.get_text("text")
        doc.close()
        return pdf_text
    except Exception as e:
        return f"Error extracting text: {e}"
    
pdf_path = "Landon-Hotel.pdf"
extracted_text = extract_text_from_pdf(pdf_path)

file = open("pdf_text", "w", encoding='utf-8')
file.write(extracted_text)

"""