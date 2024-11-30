import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint as pp
import time


def p(*args: any) -> None:
    """Функция печати.Строка с пунктуацией. Печатает в консоль."""
    print(*args)


# os.chdir(r"C:\dev\selentest")
path = os.getcwd()


def get_one_inn() -> list:
    """Парсер страницы nalog.ru с одного инн.Запись в csv файл."""
    old_list = []
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://egrul.nalog.ru/index.html")

    inn_form = browser.find_element(By.ID, "query")
    inn_form.send_keys("7728240240")
    inn_form.send_keys(Keys.ENTER)

    time.sleep(3)

    content = browser.find_elements(By.CLASS_NAME, "res-text")
    for item in content:
        old_list.append(item.text)

    data_list = old_list[0].split(",")

    df = pd.DataFrame(data_list)
    for i in range(2):
        df.to_csv("one_nalog.csv", index=False, encoding="utf-8", mode="a", sep=",")
    p("Файл записан")
    p()
    pp(item.text)

    # Нажимаем на кнопку получить pdf

    """
    button_get_pdf = browser.find_element(By.XPATH,
                                          "//*[@id='resultContent']/div/div[3]/button")
    button_get_pdf.click()
    time.sleep(9)
    """
    browser.close()
    return data_list


def get_form_fill(storage_list: list) -> object:
    """Создаем генератор"""
    for item in storage_list:
        yield item


inn_list = [
    "7707083893",
    "7722010233",
    "3019000955",
    "1619001435",
    "6730038826",
    "3827057400",
    "7825417221",
    "4205198180",
    "6670493271",
    "7810531490",
    "7203501069",
    "7451436096",
    "6670493137",
    "4909130290",
    "7453254158",
    "7451436096",
    "7203342267",
    "7456009370",
    "5038054357",
]
a_count = len(inn_list)
form_fill = get_form_fill(inn_list)


def foo(get_form_fill: object, old_list: list) -> None:
    """Вспомогательная функция для тестирования parse_and_write_to_csv.
    Имитирует работу функции write_to_csv."""

    func_gen = get_form_fill
    for j in range(2):
        old_list.append((f"{j}: {next(func_gen)}"))
    for item in old_list:
        p(item)

    p()
    p(old_list[-1])


def get_inn_in_cycle(browser: webdriver, form_fill: object, new_list: list) -> list:
    """Запросы в цикле"""
    inn_form = browser.find_element(By.ID, "query")
    inn_form.send_keys(next(form_fill))  # 7707083893
    inn_form.send_keys(Keys.ENTER)

    time.sleep(3)

    content = browser.find_elements(By.CLASS_NAME, "res-text")
    for info in content:
        new_list.append(info.text)


def sorting(form_fill: object) -> list:
    """Парсер сайта nalog.ru"""
    new_list = []
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://egrul.nalog.ru/index.html")

    i = 0
    count = 15
    while i < count:
        if i % 5 != 0:
            inn_form = browser.find_element(By.ID, "query")
            inn_form.send_keys(next(form_fill))  # 7707083893
            inn_form.send_keys(Keys.ENTER)
            time.sleep(3)

            content = browser.find_elements(By.CLASS_NAME, "res-text")
            for info in content:
                new_list.append(info.text)
            inn_form.clear()

        else:
            try:
                browser.close()
                time.sleep(3)
                browser = webdriver.Chrome()
                browser.maximize_window()
                browser.get("https://egrul.nalog.ru/index.html")
                inn_form = browser.find_element(By.ID, "query")
                inn_form.send_keys(next(form_fill))  # 7707083893
                inn_form.send_keys(Keys.ENTER)

                time.sleep(3)

                content = browser.find_elements(By.CLASS_NAME, "res-text")
                for info in content:
                    new_list.append(info.text)
                inn_form.clear()

            except StopIteration:
                break
        i += 1

    browser.close()

    return new_list


def run_cycle_five(form_fill: object, new_list: list) -> list:
    """5 запросов в цикле"""
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://egrul.nalog.ru/index.html")

    for j in range(5):
        inn_form = browser.find_element(By.ID, "query")
        inn_form.send_keys(next(form_fill))  # 7707083893
        inn_form.send_keys(Keys.ENTER)
        time.sleep(3)

        work_list = []
        content = browser.find_elements(By.CLASS_NAME, "res-text")
        for info in content:
            work_list.append(info.text)
            new_list.append(work_list[0].split(","))

        inn_form.clear()

    browser.close()
    for i in new_list:
        print(i[3])
    return new_list


def parse(form_fill: object) -> list:
    """Парсер сайта до определенного количества запросов"""
    old_list = []
    for i in range(3):
        list_data = run_cycle_five(form_fill, old_list)

    """
    df = pd.DataFrame(list_data, columns=['Город/Регион', 'ОГРН',
                                          'Дата присвоения', 'ИНН', 'КПП',
                                          'Директор', 'Дата прекращения'])
    df.to_csv("albums.csv", index=False, encoding="utf-8", mode="a", sep=",")
    p("Файл записан")
    p()
    """
    write_to_csv(list_data, "albums.csv")

    return list_data


def write_to_csv(data_list: list, file_name: str) -> None:
    """Запись в csv"""
    df = pd.DataFrame(
        data_list,
        columns=[
            "Город/Регион",
            "ОГРН",
            "Дата присвоения",
            "ИНН",
            "КПП",
            "Директор",
            "Дата прекращения",
        ],
    )
    df.to_csv(file_name, index=False, encoding="utf-8", mode="a", sep=",")
    p("Файл записан")


if __name__ == "__main__":
    form_fill = get_form_fill(inn_list)
    p(next(form_fill))
    p(next(form_fill))
    p(next(form_fill))
    p(next(form_fill))
    p(next(form_fill))
    p()
    p(os.getcwd())
    p("\n", "Ok")
