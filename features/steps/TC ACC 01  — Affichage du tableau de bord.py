from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when("utilisateur se rend sur account")
def step_impl(context):
    context.driver.get(context.base_url + "/account/")
    WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary-label"))
    )

@then("le solde total consolidé doit être affiché")
def step_impl(context):
    total_balance = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='total-balance'] .summary-amount"))
    )
    print("Solde total affiché :", total_balance.text)

    # Example assertion — adapt if needed
    assert "EUR" in total_balance.text