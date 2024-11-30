from ..quote_manager import load_quotes,add_quote
from ..main import main


def test_load_quotes(mocker):
    mock_file_data = "Quote 1\nQuote 2\nQuote 3\n"
    mock_open = mocker.patch("builtins.open", mocker.mock_open(read_data=mock_file_data))
    quotes = load_quotes()

    assert quotes == ["Quote 1", "Quote 2", "Quote 3"]

    mock_open.assert_called_once_with("quotes.txt", "r", encoding="utf-8")


def test_add_quote(mocker):
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)

    new_quote = "This is a new quote"
    add_quote(new_quote)

    mock_file().write.assert_called_with(f"{new_quote}\n")

def test_main_menu_invalid_input(mocker):
    # Мокаем ввод пользователя
    mock_input = mocker.patch("builtins.input", side_effect=["0", "5", "abc", "4"])  # Некорректные значения, затем выход
    mock_print = mocker.patch("builtins.print")  # Чтобы не выводить на экран

    main()

    # Проверяем, что сообщение об ошибке было выведено
    mock_print.assert_any_call("Invalid option! Please choose a number between 1 and 4.")