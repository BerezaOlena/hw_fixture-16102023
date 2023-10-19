import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireOptions
opts_chrome = ChromeOptions()
opts_firefox = FireOptions()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--browser_mode', action='store', default="headless",
                     help="By default is headless mode, but you can set --browser_mode='qui'")
    parser.addoption('--browser_window_size', action='store', default="norma",
                     help="By default is standart mode, but you can set --browser_window_size='norma'")

@pytest.fixture()
def browser(request):
    browser_mode = request.config.getoption("browser_mode")
    browser_name = request.config.getoption("browser_name")
    browser_window_size = request.config.getoption("browser_window_size")
    if browser_mode == "gui":
        print(f"\nbrowser_mode: {browser_mode}")
    elif browser_mode == "headless":
        opts_chrome.add_argument('--headless')
        opts_firefox.add_argument('--headless')
        print(f"\nbrowser_mode: {browser_mode}")
    else:
        print("must be gui or headless")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(opts_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(opts_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    if browser_window_size == "max":
        browser.maximize_window()
    elif browser_window_size == "norma":
        browser.set_window_size(1200, 800)
    else:
        print("must be max or norma")

    yield browser
    print("\nquit browser..")
    browser.quit()

#driver.maximize_window()
# Setting the window size to 1200 * 800
#driver.set_window_size(1200, 800)
# from selenium.webdriver.chrome.options import Options
# opts_chrome = Options()
#
# def pytest_addoption(parser):
#     parser.addoption('--browser_mode', action='store', default="headless",
#                      help="By default is headless mode, but you can set --browser_mode='qui")
#
#
# @pytest.fixture(autouse=True)
# def print_ok():
#     yield
#     print('\nbutton or element is OK')
#
# @pytest.fixture(scope="function")
# def browser(request):
#     print("\nstart browser for test..")
#     options = opts_chrome
#     options.add_argument('--start-maximized')
#     browser_mode = request.config.getoption("browser_mode")
#     if browser_mode == "gui":
#         print(f"\nbrowser_mode: {browser_mode}")
#     elif browser_mode == "headless":
#         options.add_argument('--headless')
#         print(f"\nbrowser_mode: {browser_mode}")
#     else:
#         print("must be gui or headless")
#     browser = webdriver.Chrome(options=options)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()




