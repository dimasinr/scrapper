import requests
from bs4 import BeautifulSoup

def geturl():
    all_urls = []

    for i in range(1, 2):
        url = f"https://badanpangan.go.id/berita?page={i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        def getblog(div_element):
            a_element = div_element.find("a")
            if a_element and "href" in a_element.attrs:
                return a_element["href"]
            return None

        array = []

        # div_class = soup.select("div.mb-5.font-bold.text-xl.text-justify")
        div_class = soup.select("h4.blog-post-title")

        for div in div_class:
            blog_url = getblog(div)
            if blog_url:
                array.append(blog_url)

        all_urls.extend(array)

    return all_urls

all_urls = geturl()
for url in all_urls:
    print(url)
