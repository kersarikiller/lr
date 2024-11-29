import pytest
import builtins
from person1.quote_manager import load_quotes,add_quote
from person1.main import main

def test_load_quotes_file_not_found(tmp_path):
    """Тестирует, выбрасывается ли ошибка, если файл не найден."""
    # Создаём путь к несуществующему файлу
    non_existent_file = tmp_path / "non_existent_quotes.txt"

    # Убедитесь, что файла точно нет
    assert not non_existent_file.exists()

    # Ожидаем, что функция выбросит FileNotFoundError
    with pytest.raises(FileNotFoundError):
        load_quotes(file_path=str(non_existent_file))

def test_add_quote(mocker):
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)

    new_quote = "This is a new quote"
    add_quote(new_quote)

    mock_file().write.assert_called_with(f"{new_quote}\n")

def test_main_menu_invalid_input(mocker):
    # Мокаем ввод пользователя
    mocker.patch("builtins.input", side_effect=["0", "5", "abc", "4"])  # Некорректные значения, затем выход
    mocker.patch("builtins.print")  # Чтобы не выводить на экран

    main()

    # Проверяем, что сообщение об ошибке было выведено
    builtins.print.assert_any_call("Invalid option! Please choose a number between 1 and 4.")