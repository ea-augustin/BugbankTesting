import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from helpers.credentials import URLLOGIN, EMAIL, UPDATEDPASSWORD



# ---------------------------
#   TC AUTH 07 — Mot de passe incorrect
# ---------------------------

@given("un compte existant")
def step_impl(context):
    context.valid_email = EMAIL
    context.invalid_password = UPDATEDPASSWORD


@when("l’utilisateur saisit un email valide")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-email']").send_keys(context.valid_email)


@when("saisit un mot de passe incorrect")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-password']").send_keys(context.invalid_password)


@when("l’utilisateur tente de se connecter")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='btn-login']").click()


@then("un message d’erreur doit être affiché 'Mot de passe incorrect.'")
def step_impl(context):
    error = context.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert "mot de passe incorrect" in error.lower()


@then("session ne doit être créée")
def step_impl(context):
    time.sleep(1)
    assert "dashboard" not in context.driver.current_url.lower()