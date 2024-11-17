import random

def load_quotes():
    with open('quotes.txt', 'r', encoding='utf-8') as f:
        return [quote.strip() for quote in f.readlines()]

def random_quote(quotes):
    return random.choice(quotes)
