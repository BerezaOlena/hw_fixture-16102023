from selenium.webdriver.common.by import By
import pytest

link = "https://anc.ua/"


class TestAncheadermenu():

    @pytest.mark.smoke
    def test_img_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//img[@src='https://storage.googleapis.com/static-storage/logo.svg']")

    @pytest.mark.smoke
    def test_catalog_menu_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//button[@class='button button-yellow-light text-size-16 weight-600 padding-10']")

    @pytest.mark.search
    def test_search_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//input[@class='input-search']")

    @pytest.mark.user
    def test_history_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href='/profile/history']")

    @pytest.mark.user
    def test_favorite_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href='/profile/favorites']")

    @pytest.mark.user
    def test_user_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//div[@class='row column v-center gap-5']")

    @pytest.mark.user
    def test_cart_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@title='Кошик']")


# pytest -s test_hw_16102023.py
# pytest -s -v -m "smoke" test_hw_16102023.py
# pytest -s -v -m "search" test_hw_16102023.py
# pytest -s -v -m "user" test_hw_16102023.py
# pytest -s -v --browser_name="firefox" --browser_mode="gui" --browser_window_size="max" test_hw_16102023.py


