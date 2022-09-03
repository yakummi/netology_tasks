import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {'User-Agent': UserAgent().chrome}

MAIN_LINK = 'https://habr.com'

# <дата> - <заголовок> - <ссылка>

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)

soup = BeautifulSoup(response.text, 'html.parser')

scope = soup.find_all('article', 'tm-articles-list__item')

# print(scope)

for e in scope:
    try:
        # title = e.find('a', 'tm-article-snippet__title-link').text
        # print(title)
        # date = e.find('span', 'tm-article-snippet__datetime-published').text
        # print(date)
        tags = e.find('a', "tm-article-snippet__hubs-item-link")
        tags = [tag.text.strip() for tag in tags]
        # print(tags)
        for tag in tags:
            if tag in KEYWORDS:
                title = e.find('a', 'tm-article-snippet__title-link').text
                date = e.find('span', 'tm-article-snippet__datetime-published').text
                link = e.find('a', 'tm-article-snippet__title-link').get('href')
                print(f'{date} - {title} - {MAIN_LINK+link}')
    except Exception as _ex:
        pass