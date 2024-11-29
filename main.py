from person1.quote_manager import load_quotes, random_quote, add_quote

def menu():
    print("1. Show all quotes")
    print("2. Add a new quote")
    print("3. Choose a random quote")
    print("4. Exit")

def main():
    q = load_quotes()
    while True:
        menu()
        choice = input("Choose an option: ")
        if choice == "1":
            for quote in q:
                print(quote)
        elif choice == "2":
            quote = input("Enter a quote: ")
            add_quote('\n' + quote)
        elif choice == "3":
            print(random_quote(q))
        elif choice == "4":
            break

if __name__ == '__main__':
    main()