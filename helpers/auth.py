from selenium.webdriver.common.by import By

def login(context, email, password):
    context.driver.get("https://testapp.campus-eni.fr/auth/login")
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-email']").send_keys(email)
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-password']").send_keys(password)
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='btn-login']").click()