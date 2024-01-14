from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data

user_list = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
password = 'secret_sauce'

login_locator = "//input[@id='user-name']"
password_locator = "//input[@id='password']"
login_button_locator = "//input[@id='login-button']"
error_locator = "//h3[@data-test='error']"


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def authorization_fill(self, login, password):
        login_input = self.driver.find_element(By.XPATH, login_locator)
        password_input = self.driver.find_element(By.XPATH, password_locator)
        login_button = self.driver.find_element(By.XPATH, login_button_locator)
        login_input.send_keys(login)
        password_input.send_keys(password)
        login_button.click()
        if self.driver.current_url == data.main_url:
            locked_error_message = self.driver.find_element(By.XPATH, error_locator)
            data.error_message = locked_error_message.text
            performance_glitch = WebDriverWait(self.driver, 15).until(EC.url_changes(data.shopping_url))
            data.performance_glitch = performance_glitch
