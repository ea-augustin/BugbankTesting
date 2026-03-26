from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Create the browser ONCE for all scenarios
    context.driver = webdriver.Chrome(options=chrome_options)

    # Base URL for your BugBank instance
    context.base_url = "https://testapp.campus-eni.fr"


def after_all(context):
    context.driver.quit()