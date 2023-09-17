import json
from mongoengine import connect
from models import Author, Quote
from connect import create_connect

create_connect()

def load_data():
    with open('authors.json', 'r', encoding='utf-8') as file:
        authors_data = json.load(file)

    for author_data in authors_data:
        author = Author(**author_data)
        author.save()

    with open('quotes.json', 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)

    for quote_data in quotes_data:
        author_name = quote_data['author']
        author = Author.objects(fullname=author_name).first()
    
        if author:
            quote_data['author'] = author
            quote = Quote(**quote_data)
            quote.save()

    print("Data has been successfully loaded into MongoDB Atlas.")
