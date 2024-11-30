import re


def p(*args) -> None:
    """Функция печати. Строка с пунктуацией. Печатает в консоль."""
    print(*args)


class Color:
    BOLD = "\033[1m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLACK = "\033[30m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
    GRAY = "\033[90m"


def simple_print() -> None:
    """Вывод на печать цветного текста"""
    p(Color.BOLD + "Hello, World!" + Color.END)
    print(Color.BOLD + Color.DARKCYAN + "Hello, World!" + Color.END)
    p()


def print_format() -> None:
    """Вывод на печать цветного текста."""
    print(
        "This is how the {}bold{} text looks like in Python".format(
            "\033[1m", "\033[0m"
        )
    )
    p("Вот как выглядит {}жирный текст в Python.{}".format("\033[1m", "\033[0m"))
    p()


def print_re() -> None:
    """Вывод на печать цветного текста."""
    st = "Придет осень и спросит"
    wordlist = re.sub("[^\\w]", " ", st).split()
    make_bold = lambda x: Color.BOLD + x + Color.END
    boldlist = list(map(make_bold, wordlist))

    print(boldlist)
    print(*boldlist)
    p()


def main() -> None:
    """Основная функция. Точка входа в программу."""
    simple_print()
    print_format()
    print_re()


if __name__ == "__main__":
    main()
