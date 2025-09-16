# make sure to change starts with in the extract_hrefs function to match the hrefs you want to extract
from bs4 import BeautifulSoup

def extract_hrefs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    hrefs = {a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('https://')}
    
    return hrefs

def save_hrefs_to_file(hrefs, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for href in hrefs:
            file.write(f"{href}\n")

# Example usage
file_path = 'input.html'
output_file = 'hrefs.txt'
hrefs = extract_hrefs(file_path)
save_hrefs_to_file(hrefs, output_file)