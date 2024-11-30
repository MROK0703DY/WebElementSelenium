import pandas as pd
from openpyxl.workbook import Workbook


def p(*args):
    """Функция печати.Строка с пунктуацией.Печатает в консоль."""
    print(*args)


def to_csv_1() -> None:
    """Запись в csv"""
    pd.DataFrame({"col1": [1, 2], "col2": [3, 4]}).to_csv("albums.csv", index=False)
    p("""Файл записан""")


def to_csv() -> None:
    """Запись в csv. Использование индексов.Создаем колонки."""
    name = [
        "Rocka Rolla",
        "Sad Wings of Destiny",
        "Sin After Sin",
        "Stained Class",
        "Killing Machine",
    ]
    year = [1974, 1976, 1977, 1978, 1978]
    albums_dict = {"album": name, "release_year": year}

    albums_df = pd.DataFrame(albums_dict)
    albums_df.index = ["a", "b", "c", "d", "e"]
    print(albums_df)

    albums_df.to_csv("albums.csv")
    p("""Файл записан""")

    albums_df_2 = pd.DataFrame(
        [
            {"album": "Point of Entry", "year": 1981},
            {"album": "Screaming for Vengeance", "year": 1982},
        ],
        columns=["year", "album"],
    )
    p()
    p(albums_df_2)


def to_xlsx() -> None:
    """Запись в xlsx"""
    # Создаем датафрейм
    data = {
        "Имя": [
            "Анна",
            "Петр",
            "Мария",
            "Rocka Rolla",
            "Sad Wings of Destiny",
            "Sin After Sin",
            "Stained Class",
            "Killing Machine",
        ],
        "Возраст": [25, 30, 35, 1974, 1976, 1977, 1978, 1978],
        "Город": ["Москва", "Санкт-Петербург", "Киев", "a", "b", "c", "d", "e"],
    }
    df = pd.DataFrame(data)

    # Сохраняем данные в файл Excel
    df.to_excel(
        "C:\\pycharm\\PycharmProjects\\pycharm_library\\pycharm_library\\new\\данные.xlsx",
        index=False,
        sheet_name="Список первой отчетности",
    )
    p("""Файл записан""")


def main() -> None:
    """Главная функция исполнения.Точка входа в программу."""
    to_xlsx()
    p()
    p("ok")


if __name__ == "__main__":
    main()
