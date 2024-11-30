from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd


def p(*args) -> None:
    """Функция печати.Строка с пунктуацией.Печатает в консоль."""
    print(*args)


def run_test() -> None:
    """Функция тестирования."""
    driver = webdriver.Chrome()
    driver.get("http://tutorialsninja.com/demo/")
    driver.maximize_window()
    elem = driver.find_element(By.NAME, "search")
    elem.clear()

    elem.send_keys("iphone")
    elem.send_keys(Keys.RETURN)

    add_to_cart = driver.find_element(
        By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]'
    )
    add_to_cart.click()

    shopping_cart_link = driver.find_element(
        By.XPATH, '//*[@id="top-links"]/ul/li[4]/a'
    )
    shopping_cart_link.click()

    assert "product 11" in driver.page_source, "Товар не загружен"
    sleep(5)

    p("Идет тестирование")

    driver.close()
    driver.quit()
    p("""Тест пройден""")


def to_csv() -> None:
    """Запись в csv."""
    pd.DataFrame({"col1": [1, 2], "col2": [3, 4]}).to_csv("test.csv", index=False)
    p("""Файл записан""")


def main() -> None:
    """Главная функция исполнения.Точка входа в программу."""
    run_test()
    p("ok")


if __name__ == "__main__":
    main()
