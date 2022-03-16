import requests
from bs4 import BeautifulSoup as soup


def get_content_string(url):
    page = requests.get(url)
    page_soup = soup(page.content, 'html.parser')
    print(page_soup)

    containers = page_soup.find_all("script", {"type": "application/ld+json"})

    article_list = []
    for container in containers:
        for dictionary in container:
            article_list.append(dictionary)

    article_list[0:2] = [''.join(article_list[0:2])]
    content_string = article_list[0]
    print(content_string)


get_content_string("https://www.nytimes.com/section/technology")
