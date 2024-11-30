from unittest import TestCase, main
from new.up_date_value import UpdateValue


def p(*args) -> None:
    """Функция печати.Строка с пунктуацией.Печатает в консоль."""
    print(*args)


player = {
    "status": "ACTIVE",
    "balance": 100,
    "localize": {
        "en": {"nickname": "SolweMe", "countries": {"UA": 3}},
        "ru": {"nickname": "SolweMy"},
    },
    "avatar": "https://google.com",
}


class UpDateValueTest(TestCase):
    """Класс тестирования для класса UpdateValue."""

    def setUp(self) -> None:
        """Метод инициализации."""
        self.updater = UpdateValue()

    def test_update_inner_value1(
        self, mutable_dict=player, keys_list=["status"], value=8080
    ) -> dict:
        """Метод меняет значение заданного ключа в словаре."""
        up = UpdateValue()
        up.update_inner_value(mutable_dict=player, keys_list=["status"], value=8080)
        self.assertEqual(player["status"], 8080)

    def test_update_inner_value2(
        self, mutable_dict=player, keys_list=["localize", "ru", "nickname"], value=8080
    ) -> dict:
        """Метод меняет значение заданного ключа в словаре
        в третьей вложенной структуре."""
        up = UpdateValue()
        up.update_inner_value(player, ["localize", "ru", "nickname"], "Sam")
        self.assertEqual(player["localize"]["ru"]["nickname"], "Sam")

    def test_different_types(
        self, mutable_dict=player, keys_list=1000, value=8080
    ) -> dict:
        """Тестирование несоответствия типов данных."""
        with self.assertRaises(TypeError) as e:
            up = UpdateValue()
            up.update_inner_value(player, 1000, 8080)
        self.assertEqual("object of type 'int' has no len()", e.exception.args[0])

    def test_parameters_not_passed(
        self, mutable_dict=player, keys_list=1000, value=8080
    ) -> dict:
        """Не переданы параметры."""
        with self.assertRaises(TypeError) as e:
            up = UpdateValue()
            up.update_inner_value()
        self.assertEqual(
            "UpdateValue.update_inner_value() missing 3 required positional arguments: 'mutable_dict', 'keys_list', and 'value'",
            e.exception.args[0],
        )

    def test_replacing_items_in_a_list(
        self, a_list=[1, 2, 3], old_value=2, new_value="two"
    ) -> None:
        """Метод заменяет одно значение в списке на новое.Список не меняется."""
        self.assertEqual(
            UpdateValue.replacing_items_in_a_list.__doc__,
            "Метод заменяет одно значение в списке на новое.Список не меняется.",
        )
        self.assertEqual(
            [new_value if x == old_value else x for x in a_list], [1, "two", 3]
        )

    def test_replacement_by_specific_indices_list(
        self,
        a_list=["хорошо", "удовл", "плохо", "плохо", "хорошо"],
        b_list=[1, 2, 3],
        value="отлично",
    ) -> None:
        """Метод заменяет несколько элементов в списке на одно заданное
        значение по заданным индексам.
        Список не меняется."""
        self.assertEqual(
            UpdateValue.replacement_by_specific_indices_list.__doc__[:60],
            """Метод заменяет несколько элементов в списке на одно заданное""",
        )
        self.assertEqual(
            [value if idx in b_list else x for idx, x in enumerate(a_list)],
            ["хорошо", "отлично", "отлично", "отлично", "хорошо"],
        )

    def test_multiple_substitution_list(
        self,
        a_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        a_dict={7: "Семь", 2: "Два", 10: "Десять"},
    ) -> None:
        """Метод заменяет несколько элементов в списке.
        Список не меняется."""
        self.assertEqual(
            UpdateValue.multiple_substitution_list.__doc__,
            """Метод заменяет несколько элементов в списке.\n        Список не меняется.""",
        )
        self.assertEqual(
            [a_dict.get(x, x) for x in a_list],
            [1, "Два", 3, 4, 5, 6, "Семь", 8, 9, "Десять"],
        )

    def test_remove_dups(self) -> None:
        """Удаление дубликатов из списка, сохраняя порядок."""
        numbers = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5, "sam", "sam", "pip", "pip"]
        expected_result = [1, 2, 3, 5, 6, "sam", "pip"]
        self.assertEqual(self.updater.remove_dups(numbers), expected_result)
        self.assertEqual(
            UpdateValue.remove_dups.__doc__,
            """Удаление дубликатов из списка, сохраняя порядок.""",
        )

    def test_remove_dups_empty_list(self) -> None:
        """Удаление дубликатов из пустого списка."""
        numbers = []
        expected_result = []
        self.assertEqual(self.updater.remove_dups(numbers), expected_result)

    def test_remove_dups_no_duplicates(self) -> None:
        """Удаление дубликатов из списка без дубликатов."""
        numbers = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(self.updater.remove_dups(numbers), expected_result)

    def test_creation_of_matrix(self) -> None:
        """Создание матрицы."""
        expected_result = [
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
        ]
        self.assertEqual(self.updater.creation_of_matrix(5, 6), expected_result)
        self.assertEqual(UpdateValue.creation_of_matrix.__doc__, "Создание матрицы.")

    def test_matrix_assembly(self) -> None:
        """Сборка матрицы."""
        matrix = [
            [0, 0, 0],
            [1, 1, 1],
            [2, 2, 2],
        ]
        expected_result = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        self.assertEqual(self.updater.matrix_assembly(matrix), expected_result)
        self.assertEqual(UpdateValue.matrix_assembly.__doc__, "Сборка матрицы.")


if __name__ == "__main__":
    main()
