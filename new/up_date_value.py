import sys
from pprint import pprint as pp
import re
import random


def p(*args) -> None:
    """Функция печати.Строка с пунктуацией.Печатает в консоль."""
    print(*args)


class UpdateValue:
    """Класс UpdateValue изменяет словари, списки.
    Заменяет одно или несколько значений
    в списке."""

    count = 0

    def __init__(self) -> None:
        self.__class__.count += 1

    def update_inner_value(
        self, mutable_dict: dict, keys_list: list, value: any
    ) -> dict:
        """Метод меняет значеня заданных ключей в словаре.
        Создает новые ключи.
        Меняет значения самих ключей.
        Словарь изменяется."""
        if len(keys_list) < 2:
            mutable_dict[keys_list[0]] = value
        else:
            temp = mutable_dict
            end_key = keys_list.pop()
            for item in keys_list:
                if item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[end_key] = value
        return mutable_dict

    def replacing_items_in_a_list(
        self, a_list: list, old_value: any, new_value: any
    ) -> list:
        """Метод заменяет одно значение в списке на новое.Список не меняется."""
        a_list = [new_value if x == old_value else x for x in a_list]
        return a_list

    def replacement_by_specific_indices_list(
        self, a_list: list, b_list: list, value: any
    ) -> list:
        """Метод заменяет несколько элементов в списке на одно заданное
        значение по заданным индексам.
        Список не меняется."""
        a_list = [value if idx in b_list else x for idx, x in enumerate(a_list)]
        return a_list

    def multiple_different_substitutions_list(
        self, a_list: list, b_list: list, c_list: list
    ) -> list:
        """Метод заменяет несколько элементов в списке на определенные
        значения по заданным индексам.
        Список изменяется."""
        for elem in b_list:
            a_list[elem] = c_list.pop()
        return a_list

    def multiple_substitution_list(self, a_list: list, a_dict: dict) -> list:
        """Метод заменяет несколько элементов в списке.
        Список не меняется."""
        a_list = [a_dict.get(x, x) for x in a_list]
        return a_list

    def reverse_the_list(self, a_list: list) -> list:
        """Переворачиваем список в обратном порядке.
        Список не меняется."""
        new_list = a_list[::-1]
        return new_list

    def getting_data_by_indexes_from_a_list(
        self, a_list: list, indices_to_replace: list
    ) -> list:
        """Возвращает список элементов из определенного списка по заданным индексам"""
        list_data = [a_list[x] for x in indices_to_replace]
        return list_data

    def getting_data_by_indexes_gen(
        self, a_list: list, indices_to_replace: list
    ) -> object:
        """Возвращает генератор из определенного списка по заданным индексам"""
        list_data = [a_list[x] for x in indices_to_replace]
        for i in list_data:
            yield i

    def reverse_the_string(self, a_string: str) -> str:
        """Переворачиваем строку в обратном порядке."""
        return a_string[::-1]

    def remove_dups(self, a_list: list) -> list:
        """Удаление дубликатов из списка, сохраняя порядок."""
        # numbers = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5, "sam", "sam", "pip", "pip"]
        numbers_unique = list(dict.fromkeys(a_list))
        return numbers_unique

    def remove_dups_dict1(self, a_list: list) -> list:
        """удаление дубликатов в списке словарей."""
        new = [dict(s) for s in set(frozenset(d.items()) for d in a_list)]
        return new

    def remove_dups_dict2(self, a_list: list) -> list:
        """Удаление дубликатов в списке словарей."""
        new = list(map(dict, set(tuple(sorted(e.items())) for e in a_list)))
        return new

    def get_pythonru(self, text: str) -> object:
        """
        Этот генератор создает последовательность
        значений True:
        по одному на каждое найденное слово pythonru
        Также для наглядности он выводит обработанные слова
        """
        text = re.split("[., ]+", text)
        for word in text:
            print(word)
            if word == "pythonru":
                p()
                p("Ключевое слово: pythonru")
                yield True

    test_get_pythonru = """
    text = "В Интернете есть множество сайтов, \
            но только один pythonru. \
            Программа никогда не прочтет \
            последнее предложение."
    result = "не найден"
    up.get_pythonru(text)
    for j in up.get_pythonru(text):
        result = "найден"
        break

    print('Результат поиска: %s' % result)
    """

    def creating_a_set(self, a_list: list) -> set:
        """Создание и использование Set - множества из списка."""
        unique_vowels = {i for i in a_list}
        # if i in 'aeiou'
        return unique_vowels

    def creating_a_dict(self) -> dict:
        """Создание и использование Dict - словаря из списка."""
        squares = {i: i * i for i in range(10)}
        return squares

    def get_unique_data(self) -> list:
        """Возвращает список с уникальными значениями.
        Вложенный генератор с условием."""

        def get_weather_data():
            """Возвращает случайное значение температуры"""
            return random.randrange(90, 110)

        hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
        return hot_temps

    def creation_of_matrix(self, x: int, y: int) -> list:
        """Создание матрицы."""
        matrix = [[i for i in range(x)] for _ in range(y)]
        return matrix

    def matrix_assembly(self, a_matrix: list) -> list:
        """Сборка матрицы."""
        return [num for row in a_matrix for num in row]

    def get_sum_gen(self, x: int) -> object:
        """Используйте генераторы для больших наборов данных."""
        # return sum([i * i for i in range(x)])
        return sum(map(lambda i: i * i, range(x)))

    def info_doc(self) -> None:
        """Информация о документации."""
        p(up.__doc__.replace("\n    ", ""), "\n")
        doc1 = up.update_inner_value.__doc__.replace("\n    ", "")
        p(f"update_inner_value. Этот {doc1}")
        p()
        text = [
            "Принимает на вход словарь, список и значение",
            "Если в списке один элемент, меняется значение ключа на первом уровне вложенности",
            "Если такого ключа нет, он создается",
            "Если в списке несколько элементов: ",
            "последний меняет значение этого ключа",
            "Если такого ключа нет, он создается",
            "Остальные элементы - это ключи",
            "Мы проваливаемся до нужного уровня вложенности",
        ]
        for el in text:
            p(el)

        p()
        doc2 = up.replacing_items_in_a_list.__doc__
        p(f"replacing_items_in_a_list. Этот {doc2}")
        p()
        doc3 = up.replacement_by_specific_indices_list.__doc__.replace("\n      ", "")
        p(f"replacement_by_specific_indices_list. Этот {doc3}")
        p()
        doc4 = up.multiple_different_substitutions_list.__doc__.replace("\n      ", "")
        p(f"multiple_different_substitutions_list. Этот {doc4}")
        p()
        doc5 = up.multiple_substitution_list.__doc__.replace("\n      ", "")
        p(f"multiple_substitution_list. Этот {doc5}")
        p()
        doc6 = up.reverse_the_list.__doc__.replace("\n      ", "")
        p(f"reverse_the_list. {doc6}")
        p()
        doc7 = up.getting_data_by_indexes_from_a_list.__doc__
        p(f"getting_data_by_indexes_from_a_list. {doc7}")
        p()
        doc8 = up.getting_data_by_indexes_gen.__doc__
        p(f"getting_data_by_indexes_gen. {doc8}")
        p()
        doc9 = up.reverse_the_string.__doc__
        p(f"reverse_the_string. {doc9}")
        p()
        doc10 = up.remove_dups.__doc__
        p(f"remove_dups. {doc10}")
        p()
        doc11 = up.remove_dups_dict1.__doc__
        p(f"remove_dups_dict1. {doc11}")
        p()
        doc12 = up.remove_dups_dict2.__doc__
        p(f"remove_dups_dict2. {doc12}")
        p()
        doc13 = up.get_pythonru.__doc__
        p(f"get_pythonru. {doc13}")
        p()
        doc14 = up.creating_a_set.__doc__
        p(f"creating_a_set. {doc14}")
        p()
        doc15 = up.creating_a_dict.__doc__
        p(f"creating_a_dict. {doc15}")
        p()
        doc16 = up.get_unique_data.__doc__
        p(f"get_unique_data. {doc16}")
        p()
        doc17 = up.creation_of_matrix.__doc__
        p(f"creation_of_matrix. {doc17}")
        p()
        doc18 = up.matrix_assembly.__doc__
        p(f"matrix_assembly. {doc18}")
        p()
        doc19 = up.get_sum_gen.__doc__
        p(f"get_sum_gen. {doc19}")
        p()


player = {
    "status": "ACTIVE",
    "balance": 100,
    "localize": {
        "en": {"nickname": "SolweMe", "countries": {"UA": 3}},
        "ru": {"nickname": "SolweMy"},
    },
    "avatar": "https://google.com",
}


def main() -> None:
    """Главная функция исполнения.Точка входа в программу."""
    p(f"Путь к инерпретатору: {sys.executable}")
    p()
    up = UpdateValue()
    pp(up.remove_dups_dict1.__doc__)

    p()


if __name__ == "__main__":
    main()
    p()
