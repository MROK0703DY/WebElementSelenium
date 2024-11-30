from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

title = "Selenium + Python = автоматизация тестирования веб-сайтов |\
    Селениум + Питон"
link = "https://www.youtube.com/watch?v=iEmv_nIvFp4&ab_channel=%D0%9D%D0%B0%D0%B4%D0%B5%D0%B6%D0%BD%D0%BE%D0%B5%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5"
link_vk = "https://vk.com/video240838576_456240505"
запуск_unittests = """
python -m unittest discover -s C:\dev\selentest\ tests -p *_test.py in C:\dev
"""


def p(*args) -> None:
    """Функция печати.Строка с пунктуацией.Печатает в консоль."""
    print(*args)


def test_run() -> None:
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
    sleep(3)
    driver.close()
    driver.quit()
    p("""Тест пройден""")


def main() -> None:
    """Главная функция исполнения.Точка входа в программу."""
    test_run()
    p("ok")


if __name__ == "__main__":
    main()
