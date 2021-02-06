from selenium.webdriver.remote.webdriver import WebDriver
from get_driver import chrome


class Crawler:
    def __init__(self, code: str):
        self.driver: WebDriver = chrome(chrome_debug=False)
        self.code = code

    def go(self) -> None:
        d = self.driver
        d.get(f"https://shoppinglive.naver.com/lives/{self.code}")
        d.implicitly_wait(10)
        d.quit()

# https://view.shoppinglive.naver.com/lives/67910?