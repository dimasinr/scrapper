import re
import requests
import openpyxl
from bs4 import BeautifulSoup

from checkurl import geturl

def scraping_data(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            article_element = soup.find("article")

            if article_element:
                return article_element.prettify()
            else:
                print("tidak ada tag article : ", url)
                return None
        else:
            print("Gagal get content web. status:", response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print("Error : ", e)
        return None

def save_to_excel(contents, file_name):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    for idx, content in enumerate(contents, start=1):
        soup = BeautifulSoup(content, "html.parser")

        # Find the specific div element and extract its text
        div_element = soup.find("div", class_="sm:text-sm md:text-2xl lg:text-5xl font-bold")
        if div_element:
            div_text = div_element.text.strip()
        else:
            div_text = "No text found in the div element."

        sheet.cell(row=idx, column=1, value=content)
        sheet.cell(row=idx, column=2, value=div_text)

    workbook.save(file_name)
    print("Data berhasil disimpan : ", file_name)

def cleanparser(html_text):
    clean_html = re.sub(r'(?<=>)\"(?=<)', '', html_text)
    return clean_html

urls = geturl()
print(urls)

isi_content = []
for url in urls:
    content = scraping_data(url)
    if content:
        isi_content.append(content)

if isi_content:
    save_to_excel(isi_content, "coba lgi zzzz.xlsx")
else:
    print("Gagal scraping.")
