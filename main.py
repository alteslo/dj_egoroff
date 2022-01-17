import requests

from bs4 import BeautifulSoup

url = 'https://www.imdb.com/title/tt0068646/'
if 'www.imdb.com/title' not in url:
    print('Invalid movie page!')
else:
    movi_description = {}
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'}).content
    soup = BeautifulSoup(response, 'html.parser')

    h_link = soup.find('h1', "TitleHeader__TitleText-sc-1wu6n3d-0")
    movi_description["title"] = h_link.text

    h_link = soup.find('span', "GenresAndPlot__TextContainerBreakpointXL-sc-cum89p-2")
    movi_description["description"] = h_link.text

    print(movi_description)
