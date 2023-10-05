from requests import get
from bs4 import BeautifulSoup
import json

quotes_json_file = 'quotes.json'
authors_json_file = 'authors.json'
quotes_data = []
authors_data = []

for i in range(1, 11):
    url = f'http://quotes.toscrape.com/page/{i}/'
    req = get(url)
    text = req.text
    soup = BeautifulSoup(text, 'html.parser')
    quote_elements = soup.find_all('div', class_='quote')

    for quote_element in quote_elements:
        quote_text = quote_element.find('span', {'class': 'text'}).text.strip()
        author = quote_element.find('small', {'class': 'author'}).text.strip()

        quote_data = {
            'quote': quote_text,
        }

        quotes_data.append(quote_data)

        if author not in authors_data:
            authors_data.append(author)

with open(quotes_json_file, 'w') as quotes_fh:
    json.dump(quotes_data, quotes_fh, indent=4)

with open(authors_json_file, 'w') as authors_fh:
    json.dump(authors_data, authors_fh, indent=4)

print(f'Цитаты сохранены в {quotes_json_file}')
print(f'Авторы сохранены в {authors_json_file}')
