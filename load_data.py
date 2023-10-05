import json
from mongoengine import connect
from models import Author, Quote
from connect import create_connect

create_connect()

def load_quotes_data():
    with open('quotes.json', 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)

    for quote_data in quotes_data:
        author_name = quote_data.get('author', 'Unknown Author')  
        author = Author.objects(fullname=author_name).first()
        quote_text = quote_data['quote']

        if author:
            quote = Quote(quote=quote_text, author=author)
            quote.save()
        else:
            quote = Quote(quote=quote_text)
            quote.save()

    print("Данные о цитатах успешно загружены в MongoDB Atlas.")

load_quotes_data()
