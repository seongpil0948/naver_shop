from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


def chrome(chrome_debug: bool = False) -> WebDriver:
    options = webdriver.ChromeOptions()
    if chrome_debug == False:
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('--disable-gpu')

    driver: WebDriver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        chrome_options=options,
        keep_alive=False
    )
    driver.maximize_window()
    return driver
