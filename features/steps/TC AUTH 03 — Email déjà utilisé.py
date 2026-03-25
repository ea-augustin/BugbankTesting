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
# WHEN : L’utilisateur ouvre la page d’inscription
# ---------------------------------------------------------
@when("l’utilisateur est sur la page /auth/register")
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
# STEP : Saisie d’un email déjà existant
# ---------------------------------------------------------
@step("saisit un nom d’utilisateur et un email déjà existant")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-username']").send_keys(EXISTING_USERNAME)
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-email']").send_keys(EXISTING_EMAIL)
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-password']").send_keys(EXISTING_PASS)
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-confirm-password']").send_keys(EXISTING_PASS)


# ---------------------------------------------------------
# THEN : Clic sur le bouton Créer mon compte
# ---------------------------------------------------------
@then("clique sur le btn Créer mon compte")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='btn-register']").click()
    time.sleep(1)


# ---------------------------------------------------------
# THEN : Message d’erreur attendu
# ---------------------------------------------------------
@then("un message d’erreur 'email déjà utilisé' doit être affiché")
def step_impl(context):
    error = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='alert-danger']"))
    )

    assert "email est deja utilise" in error.text.lower()
    print("Erreur détectée :", error.text)
    time.sleep(2)

@then("le formulaire doit être affiché à nouveau")
def step_impl(context):
    # Wait for the registration title Creer un compte>
    title = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )

    assert "creer un compte" in title.text.lower()
    print("Formulaire affiché à nouveau :", title.text)

    time.sleep(2)
