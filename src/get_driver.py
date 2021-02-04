from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def chrome(chrome_debug: bool = False):
    options = webdriver.ChromeOptions()
    if chrome_debug == False:
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(), chrome_options=options)
    driver.maximize_window()
    return driver
