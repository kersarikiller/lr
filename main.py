from quote_manager import load_quotes, random_quote

def main():
    q = load_quotes()
    print(f'random quote: {random_quote(q)}')

if __name__ == '__main__':
    main()