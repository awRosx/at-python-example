from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def authorization_fill(self, login, password):
        login_input = self.driver.find_element(By.XPATH, data.login_locator)
        password_input = self.driver.find_element(By.XPATH, data.password_locator)
        login_button = self.driver.find_element(By.XPATH, data.login_button_locator)
        login_input.send_keys(login)
        password_input.send_keys(password)
        login_button.click()
        if self.driver.current_url == data.main_url:
            locked_error_message = self.driver.find_element(By.XPATH, data.error_locator)
            data.error_message = locked_error_message.text
            performance_glitch = WebDriverWait(self.driver, 15).until(EC.url_changes(data.shopping_url))
            data.performance_glitch = performance_glitch
