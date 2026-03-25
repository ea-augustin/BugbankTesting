from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.credentials import ACTUALPASS


@when("saisit le mot de passe actuel correct")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-current-password']").send_keys(ACTUALPASS)


@when("saisit un mot de passe de confirmation différent")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-confirm-password']").send_keys("Different123!")


@then("le mot de passe actuel doit être validé")
def step_impl(context):
    page_text = context.driver.page_source.lower()
    assert "mot de passe actuel incorrect" not in page_text


@then("le système doit détecter la non correspondance")
def step_impl(context):
    error = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash-messages .alert-danger"))
    )
    assert "ne correspondent" in error.text.lower()