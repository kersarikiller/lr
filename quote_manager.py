import random

def load_quotes(file='quotes.txt'):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return [quote.strip() for quote in f.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return []
    except IOError as e:
        print(f"Error reading file '{file}': {e}")
        return []

def random_quote(quotes):
    return random.choice(quotes)

def add_quote(quote, file='quotes.txt'):
    if not quote.strip():
        print("Error: Cannot add an empty quote.")
        return
    try:
        with open(file, 'a', encoding='utf-8') as f:
            f.write(f'{quote.strip()}\n')
        print("Quote added successfully.")
    except IOError as e:
        print(f"Error writing to file '{file}': {e}")

def list_quotes_by_length(descending=False):
    quotes = load_quotes()
    sorted_quotes = sorted(quotes, key=len, reverse=descending)
    for quote in sorted_quotes:
        print(quote)