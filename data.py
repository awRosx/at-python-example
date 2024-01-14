from selenium.webdriver.chrome.service import Service

driver_path = 'C:\\resource\\chromedriver.exe'
main_url = 'https://www.saucedemo.com/'
shopping_url = 'https://www.saucedemo.com/inventory.html'

user_list = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
password = 'secret_sauce'

login_locator = "//input[@id='user-name']"
password_locator = "//input[@id='password']"
login_button_locator = "//input[@id='login-button']"
error_locator = "//h3[@data-test='error']"

link = Service(driver_path)

error_message = str
performance_glitch = bool
