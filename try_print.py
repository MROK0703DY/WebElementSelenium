"""Проверочный модуль. Вывод на печать текущей даты и времени."""

import sys
import time
import datetime
from datetime import datetime as dt
from print_bold_and_color_text import Color


NUMBER = "01 декабря"
TIME_HOUR = "00"
DAY = "ВСК"


def p(*args) -> None:
    """Функция печати. Строка с пунктуацией. Печатает в консоль."""
    print(*args)


def sys_executable() -> None:
    """Вывод на печать пути к инерпретатору."""
    print()
    print(f"Путь к интерпретатору: {sys.executable}")
    p(f"Версия Python: {sys.version}")
    print()


def get_date_one() -> None:
    """Вывод на печать текущей даты и времени."""
    x = datetime.date.isoformat(datetime.date.today())
    y = f"{x[8:]} декабря {x[:4]}"
    z = time.strftime("%H:%M:%S")
    p(f"get_date_one:  {Color.BOLD} {Color.PURPLE}{x}\n")
    p(f"                {y} {z}{Color.END}")


def get_date_two(NUMBER: str, TIME_HOUR: str, DAY: str) -> None:
    """Вывод на печать текущей даты и времени."""
    current_time = time.time()
    local_time = time.localtime(current_time)

    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", local_time)
    # print(formatted_time)
    p()
    ft = formatted_time.split()
    p(
        f"get_date_two:   {Color.BOLD}{Color.GREEN}{NUMBER} {ft[0][6:]} {TIME_HOUR}{ft[1][2:]} {DAY}{Color.END}"
    )
    p()


def get_date_three() -> None:
    """Вывод на печать текущей даты и времени."""
    d, ct = str(dt.now()).split()
    d = d.split("-")
    d[1] = "декабря"
    d = list(reversed(d))
    d = " ".join(d)
    ct = ct.split(".")[0]
    t = ct.split(":")
    t[0] = str(int(t[0]))
    t = ":".join(t)
    a_time = dt.now().strftime("%a")
    p(f"get_date_three: {Color.BOLD}{Color.BLUE}{d} {t} {a_time}{Color.END}")
    p()


def short_entry() -> None:
    """Вывод на печать текущей даты и времени."""
    a_time = dt.now().strftime("%a")
    current_time = str(dt.now()).split()[1].split(("."))[0] + " " + a_time
    date = " ".join(
        [
            "декабря" if x == "12" else x
            for x in ((str(dt.now()).split())[0].split("-")[::-1])
        ]
    )
    p(f"short_entry:    {Color.BOLD}{Color.RED}{date} {current_time}{Color.END}")
    p()


def main() -> None:
    """Главная функция.Точка входа в программу."""
    sys_executable()
    get_date_one()
    get_date_two(NUMBER, TIME_HOUR, DAY)
    get_date_three()
    short_entry()


if __name__ == "__main__":
    main()
