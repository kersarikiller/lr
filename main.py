from quote_manager import load_quotes, random_quote, add_quote
from datetime import datetime

def main():
    q = load_quotes()
    date_added = datetime.now().strftime("%Y-%m-%d")
    print(f'random quote: {random_quote(q)}', f'total quotes: {len(q)}', date_added)
    a = input('add a quote? print "y" or "n" \n')
    if a == 'y':
        add_quote(input('add a quote: \n'))


if __name__ == '__main__':
    main()