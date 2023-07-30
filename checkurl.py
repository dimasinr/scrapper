import requests
from bs4 import BeautifulSoup

def geturl():
    url = "https://badanpangan.go.id"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    def getblog(div_element):
        a_element = div_element.find("a")
        if a_element and "href" in a_element.attrs:
            return a_element["href"]
        return None

    array = []

    div_class = soup.select("div.mb-5.font-bold.text-xl.text-justify")

    for div in div_class:
        blog_url = getblog(div)
        if blog_url:
            array.append(blog_url)

    return array

