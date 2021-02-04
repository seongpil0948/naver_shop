from get_driver import chrome


class Crawler:
    def __init__(self, code: str):
        self.driver = chrome(chrome_debug=True)
        self.code = code

    def go(self):
        d = self.driver
        d.get(f"https://shoppinglive.naver.com/lives/{self.code}")
