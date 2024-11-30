from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time


def p(*args) -> None:
    """Функция печати.Строка с пунктуацией.Печатает в консоль."""
    print(*args)


n = "\n"
current_time = time.time()
local_time = time.localtime(current_time)
formatted_time = time.strftime("%H:%M:%S %d-%m-%Y", local_time)
# print(formatted_time)


class TestPython(object):

    def __init__(self, driver, lang):
        """Конструктор класса TestPython"""
        self.driver = driver
        self.lang = lang

    def parse(self) -> None:
        """Функция для парсинга тестов."""
        self.go_to_tests_page()

    def go_to_tests_page(self) -> None:
        """Функция для перехода на страницу с тестами."""
        link = ""
        self.driver.get(link)
        # elems = self.driver.find_elements(By.CLASS_NAME "a")

        # for elem in elems:
        # pass

    def bb(self) -> None:
        """Выбор языка программирования для тестирования."""
        driver = webdriver.Chrome()
        parser = TestPython(driver, "python")
        parser.parse()
        time.sleep(5)

    def clik_my(self) -> None:
        """Нажать на кнопку."""
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demoqa.com/buttons")
        btn = driver.find_element(By.CLASS_NAME, "btn-primary")
        btn.click()
        p(formatted_time, "Click btn", n)

        time.sleep(5)

        title = driver.find_element(By.TAG_NAME, "h1")
        p(formatted_time, n, "Current title: ", n, title.text)

        get_url = driver.current_url
        print("The current url is: " + str(get_url))

    def double_click(self) -> None:
        """Нажать на кнопку дважды."""
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demoqa.com/buttons")
        btn_duble = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/button"
        )
        # //*[@id="doubleClickBtn"]

        action = ActionChains(driver)
        action.double_click(btn_duble).perform()
        p(formatted_time, "Double click btn", n)


def main() -> None:
    """Основная функция.Точка входа."""
    tt = TestPython(driver=webdriver.Chrome(), lang="python")
    tt.clik_my()


if __name__ == "__main__":
    main()
