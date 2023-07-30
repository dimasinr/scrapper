import requests
from bs4 import BeautifulSoup

url = "https://badanpangan.go.id"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

div_elements = soup.select("div.mb-5.font-bold.text-xl.text-justify")
if div_elements:
    for div_element in div_elements:
        a_elements = div_element.find_all("a")
        if a_elements:
            for a_element in a_elements:
                text_in_a = a_element.text.strip()
                print(text_in_a)
        else:
            print("tidak ada tag a dalam div")
else:
    print("tidak ada tag div")
