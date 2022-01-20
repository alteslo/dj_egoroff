import requests
from bs4 import BeautifulSoup
import re


def get_soup(url):
    response = requests.get(url)
    if response:
        page_content = response.content
        soup = BeautifulSoup(page_content, 'html.parser')
        return soup
    else:
        print('Не удалось получить ссылку')


inp_url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
soup = get_soup(inp_url)

tag_titles = soup.find_all('span', "c-meta__type")

for tag_title in tag_titles:
    if 'News' == tag_title.get_text():
        title = tag_title.find_previous('h3').get_text().strip()
        news_link = f"https://www.nature.com{tag_title.find_previous('a').get('href')}"
        print(news_link)
        news_soup = get_soup(news_link)
        news_text = news_soup.find("div", "c-article-body").text.strip()
        title = re.sub(r'''[^\w\s]''', '', title)
        snake_title = title.replace(' ', '_')
        with open(f'{snake_title}.txt', 'wb') as file:
            file.write(news_text.encode())
