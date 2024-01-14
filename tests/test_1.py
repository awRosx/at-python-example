import data
from selenium import webdriver
from pages.login_page import LoginPage
import pages.login_page as login_page

driver = webdriver.Chrome(executable_path=data.driver_path)


def test_login_all_users():
    for i in login_page.user_list:
        driver.get(data.main_url)
        driver.maximize_window()
        login = LoginPage(driver)
        login.authorization_fill(i, login_page.password)
        if i == login_page.user_list[0] or i == login_page.user_list[2] or\
                i == login_page.user_list[5] or i == login_page.user_list[4]:
            assert driver.current_url == data.shopping_url
        elif i == login_page.user_list[1]:
            assert 'locked' in data.error_message
        elif i == login_page.user_list[3]:
            assert data.performance_glitch
