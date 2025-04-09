import io
import sys
from dynamic_programming.Гистограмма import get_gistograma

# тест гистограмы больше не работает, потому что я поменя чтение данных в гистограме с терминала, на файл

def test_example1(monkeypatch, capsys):
    # Пример 1:
    # Входные данные: одна строка "Hello, world!" и пустая строка для завершения ввода
    test_input = "Hello, world!\n\n"
    monkeypatch.setattr(sys, 'stdin', io.StringIO(test_input))
    get_gistograma()
    captured = capsys.readouterr().out

    # Ожидаемый вывод:
    # Первый ряд: "     #   "  (9 символов: 5 пробелов, затем '#' и 3 пробела)
    # Второй ряд: "     ##  "
    # Третий ряд: "#########"
    # Четвертая строка — отсортированные символы: "!,Hdelorw"
    expected = "     #   \n     ##  \n#########\n!,Hdelorw"
    assert captured == expected

def test_example2(monkeypatch, capsys):
    # Пример 2:
    # Многострочный ввод, завершающийся пустой строкой.
    test_input = (
        "Twas brillig, and the slithy toves\n"
        "Did gyre and gimble in the wabe;\n"
        "All mimsy were the boroвgoves,\n"
        "And the mome raths outgrabe.\n"
        "\n"
    )
    monkeypatch.setattr(sys, 'stdin', io.StringIO(test_input))
    get_gistograma()
    captured = capsys.readouterr().out

    # Ожидаемый вывод (точно такой же, как приведено в условии задачи):
    expected = (
        "         #              \n"
        "         #              \n"
        "         #              \n"
        "         #              \n"
        "         #              \n"
        "         #         #    \n"
        "         #  #      #    \n"
        "      #  # ###  ####    \n"
        "      ## ###### ####    \n"
        "      ##############    \n"
        "      ##############  ##\n"
        "#  #  ############## ###\n"
        "########################\n"
        ",.;ADTabdeghilmnorstuvwy"
    )
    assert captured == expected
