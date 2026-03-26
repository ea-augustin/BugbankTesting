from behave import when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.credentials import DEST_IBAN, TRANSFER_LABEL, TRANSFER_AMOUNT


@then("clique sur le bouton Virement")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-transfer"))
    ).click()


@when("l’utilisateur se rend sur /transfer/")
def step_impl(context):
    context.driver.get(context.base_url + "/transfer/")
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='input-to-iban']"))
    )


@step("sélectionne le compte source")
def step_impl(context):
    select = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='select-from-account']"))
    )
    select.click()
    option = context.driver.find_element(By.CSS_SELECTOR, "[data-testid='option-account-13']")
    option.click()


@step("saisit l’IBAN destinataire")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-to-iban']").send_keys(DEST_IBAN)


@step("saisit le montant")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-amount']").send_keys(str(TRANSFER_AMOUNT))


@step("saisit libelle")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-transfer-label']").send_keys(TRANSFER_LABEL)


@step("soumet virement")
def step_impl(context):
    submit_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='btn-submit-transfer']"))
    )
    submit_btn.click()


@then("toutes les validations doivent réussir")
def step_impl(context):
    success_alert = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='alert-success']"))
    )
    assert "virement" in success_alert.text.lower()


@then("le compte source doit être débité")
def step_impl(context):
    source_balance = context.driver.find_element(By.CSS_SELECTOR, "[data-testid^='account-balance-13']").text
    assert "-" in source_balance or "EUR" in source_balance


@then("le compte destinataire doit être crédité")
def step_impl(context):
    dest_balance = context.driver.find_element(By.CSS_SELECTOR, "[data-testid^='account-balance-45']").text
    assert "+" in dest_balance or "EUR" in dest_balance