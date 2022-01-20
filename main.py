import requests
from bs4 import BeautifulSoup
import string
import os


def get_soup(url):
    response = requests.get(url)
    if response:
        page_content = response.content
        soup = BeautifulSoup(page_content, 'html.parser')
        return soup
    else:
        print('Не удалось получить ссылку')


def snake_name(title):
    tt = str.maketrans(dict.fromkeys(string.punctuation))
    title = title.translate(tt)
    return title.replace(' ', '_')


def create_dir(page_num):
    try:
        os.mkdir(f'Page_{page_num}')
    except OSError:
        pass


def find_articles(page_nums, type_articles):
    for page_num in range(page_nums):
        page_num = page_num + 1
        inp_url = f'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={page_num}'
        soup = get_soup(inp_url)
        tag_titles = soup.find_all('span', "c-meta__type")
        for tag_title in tag_titles:
            if type_articles == tag_title.get_text():

                title = tag_title.find_previous('h3').get_text().strip()
                snake_title = snake_name(title)

                news_link = f"https://www.nature.com{tag_title.find_previous('a').get('href')}"
                news_soup = get_soup(news_link)
                news_text = news_soup.find("div", "c-article-body").text.strip()

                create_dir(page_num)
                with open(f'Page_{page_num}/{snake_title}.txt', 'wb') as file:
                    file.write(news_text.encode())
    print('Saved all articles.')


page_num = int(input())
type_articles = input()

find_articles(page_num, type_articles)
