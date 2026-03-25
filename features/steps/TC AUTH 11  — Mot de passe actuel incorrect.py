from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.credentials import CONFIRMUPDATEDPASSWORD


@when("saisit un mot de passe actuel incorrect")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-current-password']").send_keys("WrongPass123!")


@when("saisit un mot de passe de confirmation identique")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-confirm-password']").send_keys(CONFIRMUPDATEDPASSWORD)


@then("un message d'erreur doit être affiché")
def step_impl(context):
    error = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash-messages .alert-danger"))
    )
    assert "mot de passe actuel incorrect" in error.text.lower()