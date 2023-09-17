from mongoengine import connect
from models import Author, Quote
from connect import create_connect
from load_data import load_data


def main():
    print('hello world!')
    while True:
        user_input = input("Введите команду (например, name:Steve Martin, tag:life, exit): ").strip()
    
        if user_input.lower() == 'exit':
            break
    
        parts = user_input.split(':')
    
        if len(parts) != 2:
            print("Неверный формат команды. Попробуйте снова.")
            continue
    
        command, value = parts[0], parts[1]
    
        if command.lower() == 'name':
            author = Author.objects(fullname=value).first()
            if author:
                quotes = Quote.objects(author=author)
                for quote in quotes:
                    print(f"{quote.quote}")
            else:
                print(f"Автор с именем '{value}' не найден.")
    
        elif command.lower() == 'tag':
            quotes = Quote.objects(tags=value)
            for quote in quotes:
                print(f"{quote.quote}")
    
        elif command.lower() == 'tags':
            tags = value.split(',')
            quotes = Quote.objects(tags__in=tags)
            for quote in quotes:
                print(f"{quote.quote}")
    
        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == '__main__':
    create_connect()
    load_data()
    main()