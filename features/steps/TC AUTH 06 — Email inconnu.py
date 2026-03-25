import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from helpers.credentials import URLLOGIN, UNKNOWN_EMAIL, UNKNOWN_PASS


# ---------------------------
#   COMMON STEP
# ---------------------------

@given("l’utilisateur met sur la page de connexion")
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.driver.get(URLLOGIN)


# ---------------------------
#   TC AUTH 06 — Email inconnu
# ---------------------------

@given("aucun compte n’existe avec cet email")
def step_impl(context):
    context.unknown_email = UNKNOWN_EMAIL
    context.fake_password = UNKNOWN_PASS


@when("l’utilisateur saisit un email inconnu et un mot de passe incorrect")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-email']").send_keys(context.unknown_email)
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-password']").send_keys(context.fake_password)


@when("clique sur le bouton de connexion")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='btn-login']").click()
    time.sleep(10)

@then("un message d’erreur doit être affiché 'Email ou mot de passe incorrect")
def step_impl(context):
    # The error message is inside a div.alert.alert-danger
    error = context.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
    assert "aucun compte associe a cet email." in error.lower()



@then("aucune session ne doit être créée")
def step_impl(context):
    time.sleep(1)
    assert "dashboard" not in context.driver.current_url.lower()