from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from new.write_data_nalog import get_form_fill, write_to_csv, parse, foo, inn_list
import time
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


class WriteDataNalogTest(TestCase):
    """Класс тестирования write_data_nalog."""

    def test_get_one_inn(self) -> None:
        """Тестирование get_one_inn, без открытия браузера."""
        old_list = []
        # Инициализация головного браузера
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        # Создание экземпляра веб-драйвера
        driver = webdriver.Chrome(options=options)
        driver.get("https://egrul.nalog.ru/index.html")
        p("Браузер открыт")

        inn_form = driver.find_element(By.ID, "query")
        inn_form.send_keys("7728240240")
        inn_form.send_keys(Keys.ENTER)
        p("ИНН введен")

        time.sleep(3)

        content = driver.find_elements(By.CLASS_NAME, "res-text")
        for item in content:
            old_list.append(item.text)

        data_list = old_list[0].split(",")
        p(data_list)
        p()
        self.assertTrue(True, "Результаты поиска")
        self.assertTrue(
            True,
            "ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ\
                        'ИНВЕСТИЦИИ. НОВАЦИИ. НЕДВИЖИМОСТЬ.'",
        )
        self.assertEqual(data_list[3], " ИНН: 7728240240")
        driver.close()

    def test_get_one_inn_press_the_button(self) -> None:
        """Нажимаем на кнопку получить pdf.
        Тестирование get_one_inn, без открытия браузера."""
        # Инициализация головного браузера
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        # Создание экземпляра веб-драйвера
        driver = webdriver.Chrome(options=options)
        url = "https://solvit.space/?utm_source=yt_channel_artemshumeiko&utm_medium=organic&utm_campaign=desc_box&clckid=6a608c4e"
        driver.get(url)
        p("Браузер открыт")

        button_pdf = driver.find_element(
            By.XPATH,
            "//*[@id='__nuxt']/div/div/div[2]/div[2]/div[1]/div[2]/article[1]/div[2]/a",
        )
        button_pdf.click()
        p("Кнопка нажата")

        time.sleep(2)

        control_url = driver.current_url
        p(control_url)
        p()
        self.assertTrue(True, "ТОП вопросов по Python")
        self.assertEqual(control_url, "https://solvit.space/podborki_voprosov/19")
        driver.close()

    def test_get_form_fill(self) -> None:
        """Тестирование функции-генератора get_form_fill."""
        old_list = ["Sam", "Bob", "Kat", "Rob", "Pip", "Look", "Did", "Jen"]
        form_fill = get_form_fill(old_list)
        for item in range(5):
            p(next(form_fill))
        word = next(form_fill)
        self.assertEqual(get_form_fill.__doc__, "Создаем генератор")
        self.assertEqual(word, "Look")

    def test_run_cycle_five(
        self, form_fill=get_form_fill(inn_list), new_list=[]
    ) -> None:
        """Тестирование run_cycle_five."""
        # Инициализация головного браузера
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        # Создание экземпляра веб-драйвера
        driver = webdriver.Chrome(options=options)
        driver.get("https://egrul.nalog.ru/index.html")
        p("Браузер открыт")

        for j in range(5):
            inn_form = driver.find_element(By.ID, "query")
            inn_form.send_keys(next(form_fill))  # 7707083893
            inn_form.send_keys(Keys.ENTER)
            time.sleep(3)

            work_list = []
            content = driver.find_elements(By.CLASS_NAME, "res-text")
            for info in content:
                work_list.append(info.text)
                new_list.append(work_list[0].split(","))

            inn_form.clear()

        driver.close()
        print(new_list[0])
        self.assertTrue(True, "Результаты поиска")
        self.assertTrue(
            True,
            "ПУБЛИЧНОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО\
                        'СБЕРБАНК РОССИИ'",
        )
        self.assertEqual(new_list[0][3], " ИНН: 7707083893")

    def test_parse(self) -> None:
        """Тестирование parse.
        :return: None
        """
        old_list = []
        for i in range(3):

            foo(get_form_fill(inn_list), old_list)

        self.assertEqual(
            parse.__doc__, "Парсер сайта до определенного количества запросов"
        )
        self.assertEqual(old_list[-1], "1: 7722010233")

    def test_write_to_csv(
        self,
        data_list: list = [
            (
                [
                    1,
                ],
                [
                    2,
                ],
                [3],
                [4],
                [
                    5,
                ],
                [
                    6,
                ],
                [
                    7,
                ],
            ),
            (
                [
                    1,
                ],
                [
                    2,
                ],
                [3],
                [4],
                [
                    5,
                ],
                [
                    6,
                ],
                [
                    7,
                ],
            ),
            (
                [
                    1,
                ],
                [
                    2,
                ],
                [3],
                [4],
                [
                    5,
                ],
                [
                    6,
                ],
                [
                    7,
                ],
            ),
            (
                [
                    1,
                ],
                [
                    2,
                ],
                [3],
                [4],
                [
                    5,
                ],
                [
                    6,
                ],
                [
                    7,
                ],
            ),
            (
                [
                    1,
                ],
                [
                    2,
                ],
                [3],
                [4],
                [
                    5,
                ],
                [
                    6,
                ],
                [
                    7,
                ],
            ),
            (
                [
                    1,
                ],
                [
                    2,
                ],
                [3],
                [4],
                [
                    5,
                ],
                [
                    6,
                ],
                [
                    7,
                ],
            ),
            (
                [
                    1,
                ],
                [
                    2,
                ],
                [3],
                [4],
                [
                    5,
                ],
                [
                    6,
                ],
                [
                    7,
                ],
            ),
        ],
        file_name: str = "albums.csv",
    ) -> None:
        """Тестирование функции write_to_csv."""
        write_to_csv(data_list, file_name)
        p(reading_from_csv("albums.csv"))
        self.assertEqual(write_to_csv.__doc__, "Запись в csv")
        self.assertEqual(reading_from_csv("albums.csv"), ["col1", "col2"])


if __name__ == "__main__":
    main()
