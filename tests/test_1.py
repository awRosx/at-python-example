import data
from selenium import webdriver
from pages.login_page import LoginPage

driver = webdriver.Chrome(executable_path=data.driver_path)


def test_login_all_users():
    for i in data.user_list:
        driver.get(data.main_url)
        driver.maximize_window()
        login = LoginPage(driver)
        login.authorization_fill(i, data.password)
        if i == data.user_list[0] or i == data.user_list[2] or i == data.user_list[5] or i == data.user_list[4]:
            assert driver.current_url == data.shopping_url
        elif i == data.user_list[1]:
            assert 'locked' in data.error_message
        elif i == data.user_list[3]:
            assert data.performance_glitch
