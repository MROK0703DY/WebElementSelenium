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
        "ru": {"nickname": "SolweMy"}
    },
    "avatar": "https://google.com"
}


class UpDateValueTest(TestCase):
    """Класс тестирования для класса UpdateValue."""

    def setUp(self) -> None:
        """Метод инициализации."""
        self.updater = UpdateValue()

    def test_update_inner_value1(self, mutable_dict=player,
                                 keys_list=["status"], value=8080) -> dict:
        """Метод меняет значение заданного ключа в словаре."""
        up = UpdateValue()
        up.update_inner_value(mutable_dict=player,
                              keys_list=["status"], value=8080)
        self.assertEqual(player["status"], 8080)

    def test_update_inner_value2(self, mutable_dict=player,
                                 keys_list=["localize", "ru", "nickname"],
                                 value=8080) -> dict:
        """Метод меняет значение заданного ключа в словаре
           в третьей вложенной структуре."""
        up = UpdateValue()
        up.update_inner_value(player, ["localize", "ru", "nickname"], "Sam")
        self.assertEqual(player["localize"]["ru"]["nickname"], "Sam")

    def test_different_types(self, mutable_dict=player,
                             keys_list=1000, value=8080) -> dict:
        """Тестирование несоответствия типов данных."""
        with self.assertRaises(TypeError) as e:
            up = UpdateValue()
            up.update_inner_value(player, 1000, 8080)
        self.assertEqual("object of type 'int' has no len()", e.exception.args[0])

    def test_parameters_not_passed(self, mutable_dict=player,
                                   keys_list=1000, value=8080) -> dict:
        """Не переданы параметры."""
        with self.assertRaises(TypeError) as e:
            up = UpdateValue()
            up.update_inner_value()
        self.assertEqual("UpdateValue.update_inner_value() missing 3 required positional arguments: 'mutable_dict', 'keys_list', and 'value'", e.exception.args[0])


if __name__ == "__main__":
    main()
