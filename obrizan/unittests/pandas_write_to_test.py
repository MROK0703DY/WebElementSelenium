from unittest import TestCase, main
from new.pandas_write_to import to_csv_1, to_csv, to_xlsx
import pandas as pd
import csv


def p(*args) -> None:
    """Функция печати.Строка с пунктуацией.Печатает в консоль."""
    print(*args)


def reading_from_csv(file_name: str) -> None:
    """Чтение из файла csv."""
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        value = list(reader)[0]
    return value


def reading_from_xlsx(file_name: str, list_columns: list) -> object:
    """Чтение из файлов xlsx."""
    # Load the xlsx file
    excel_data = pd.read_excel(file_name)
    # Read the values of the file in the dataframe
    data = pd.DataFrame(excel_data, columns=list_columns)
    # Print the content
    # print(data['Имя'][0])
    return data["Имя"][0]


class PandasWriteToTest(TestCase):
    """Тестирование pandas_write_to."""

    def test_to_csv_1(self) -> None:
        """Тестирование функции to_csv_1. Запись в файл."""
        to_csv_1()
        self.assertEqual(to_csv_1.__doc__, "Запись в csv")
        self.assertEqual(reading_from_csv("albums.csv"), ["col1", "col2"])

    def test_to_csv(self) -> None:
        """Тестирование функции to_csv. Запись в файл."""
        to_csv()
        self.assertEqual(
            to_csv.__doc__, "Запись в csv. Использование индексов.Создаем колонки."
        )
        self.assertEqual(reading_from_csv("albums.csv"), ["", "album", "release_year"])

    def test_to_xlsx(self) -> None:
        """Тестирование функции to_xlsx. Запись в файл."""
        to_xlsx()
        self.assertEqual(to_xlsx.__doc__, "Запись в xlsx")
        list_columns = ["Имя", "Возраст", "Город"]
        file_name = "C:\\pycharm\\PycharmProjects\\pycharm_library\\pycharm_library\\new\\данные.xlsx"
        self.assertEqual(reading_from_xlsx(file_name, list_columns), "Анна")


if __name__ == "__main__":
    main()
