import re
from bs4 import BeautifulSoup
import requests
# from berita.models import ArtikelPertanian
# from dash.helpers.logging import logger

def do_scraping_artikel_pertanian():
    try:
        url = "https://badanpangan.go.id/berita?page=1"
        content = scraping_artikel(url=url)
        if content:
            save_or_get_artikel_pertanian(content)
            return "Scraping data successfully."
        else:
            return "No content found."
    except Exception as e:
        msg = "Failed to scraping data - %s" % str(e)
        # logger.error(msg)
        return msg

def scraping_artikel(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            article_element = soup.find("div")

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

def imageregx(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    div_element = soup.find("div", class_="bg-cover 3xl:bg-auto bg-center bg-no-repeat relative")
    if div_element:
        style_attr = div_element.get("style")
        if style_attr:
            match = re.search(r"url\('([^']+)'\)", style_attr)
            if match:
                return match.group(1)
    return None

def cleanparser(html_text):
    clean_html = re.sub(r'(?<=>)\"(?=<)', '', html_text)
    return clean_html

def save_or_get_artikel_pertanian(content):
    soup = BeautifulSoup(content, "html.parser")
    
    div_element = soup.find("div", class_="sm:text-sm md:text-2xl lg:text-5xl font-bold")
    title_text = div_element.text.strip() if div_element else "tidak ada teks"
    
    image_url = imageregx(content)
    cleaned_content = cleanparser(content)
    
    print(f"title = {title_text}")
    # ArtikelPertanian.objects.get_or_create(title=title_text, foto=image_url, content=cleaned_content)

do_scraping_artikel_pertanian()