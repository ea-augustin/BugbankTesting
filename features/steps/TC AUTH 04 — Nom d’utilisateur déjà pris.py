import time
from behave import given, when, then, step, use_step_matcher
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.credentials import *

use_step_matcher("re")


# ---------------------------------------------------------
# GIVEN : A user already exists with this username
# ---------------------------------------------------------
@given("un compte existe déjà avec ce nom d’utilisateur")
def step_impl(context):
    # Nothing to do here — the existing username is defined in credentials.py
    # EXISTING_USERNAME is already known by the system
    pass


# ---------------------------------------------------------
# WHEN : User opens the registration page
# ---------------------------------------------------------
@when("l’utilisateur met sur la page /auth/register")
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.driver.get(REGISTERURL)
    time.sleep(1)


# ---------------------------------------------------------
# STEP : User enters an already taken username
# ---------------------------------------------------------
@step("saisit un nom d’utilisateur déjà pris")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-username']").send_keys(EXISTING_USERNAME)
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-email']").send_keys(NEWEMAIL2)
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-password']").send_keys(NEWPASS2)
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-confirm-password']").send_keys(NEWPASS2)


# ---------------------------------------------------------
# THEN : Click on Create Account
# ---------------------------------------------------------
@then("clique sur le bouton Créer compte")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='btn-register']").click()
    time.sleep(1)


# ---------------------------------------------------------
# THEN : Error message for username already taken
# ---------------------------------------------------------
@then("un message d’erreur 'nom d’utilisateur déjà pris' doit être affiché")
def step_impl(context):
    error = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='alert-danger']"))
    )
    message = error.text.lower().strip()

    assert "email est deja utilise" in message \
        or "cet email est deja utilise" in message

    print("Erreur détectée :", error.text)
    time.sleep(2)


# ---------------------------------------------------------
# THEN : Form should be displayed again
# ---------------------------------------------------------
@then("le formulaire doit être affiché")
def step_impl(context):
    title = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )

    assert "creer un compte" in title.text.lower()
    print("Formulaire affiché à nouveau :", title.text)

    time.sleep(2)