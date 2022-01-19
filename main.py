import requests
from bs4 import BeautifulSoup
import string

inp_url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
response = requests.get(inp_url)
page_content = response.content
status = response.status_code
soup = BeautifulSoup(page_content, 'html.parser')

tag_titles = soup.find_all('span', "c-meta__type")

for tag_title in tag_titles:
    if 'News' in tag_title.get_text():
        title = tag_title.find_previous('h3').get_text().strip().replace(' ', '_')
        for i in string.punctuation:
            if i in title:
        news_text = tag_title.find_previous('p').get_text().strip()
        print(string.punctuation.split())
        '''with open(f'{title}.txt', 'w') as file:
            file.write(news_text)'''
