import time
from behave import given, when, then, step, use_step_matcher
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.credentials import *

use_step_matcher("re")


@when("l’utilisateur se rend sur /auth/register")
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


@step("saisit un nom d’utilisateur, un mot de passe et un mot de passe de confirmation différent")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-username']").send_keys(NEWUSERNAME3)
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-email']").send_keys(EMAIL3)
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-password']").send_keys(NEWPASS3)
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-confirm-password']").send_keys(CONFIRMPASSWORDDIFF)


@then("clique sur le bouton 'Créer mon compte'")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='btn-register']").click()
    time.sleep(5)

# -------------------------
# STEP: message
# -------------------------

@then("un message d’erreur doit être affiché 'les mots de passe ne correspondent pas'")
def step_impl(context):
    alert = WebDriverWait(context.driver, 10).until(EC.alert_is_present())
    text = alert.text.lower().strip()

    assert "les mots de passe ne correspondent pas" in text

    # Close the alert
    alert.accept()


