import random

def load_quotes(file = 'quotes.txt'):
    with open(file, 'r', encoding='utf-8') as f:
        return [quote.strip() for quote in f.readlines()]

def random_quote(quotes):
    return random.choice(quotes)

def add_quote(quote):
    with open('quotes.txt', 'a', encoding='utf-8') as f:
            f.write(f'{quote}\n')

def list_quotes_by_length(descending=False):
    quotes = load_quotes()
    sorted_quotes = sorted(quotes, key=len, reverse=descending)
    for quote in sorted_quotes:
        print(quote)