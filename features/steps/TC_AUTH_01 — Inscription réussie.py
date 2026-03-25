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


@when("l’utilisateur est sur la page d’inscription /auth/register")
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


@step("saisit un nom d’utilisateur, un email, un mot de passe et une confirmation valides")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-username']").send_keys(NEWUSERNAME2)
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-email']").send_keys(NEWEMAIL2)
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-password']").send_keys(NEWPASS2)
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-confirm-password']").send_keys(NEWPASS2)


@then("clique sur le bouton Créer mon compte")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='btn-register']").click()
    time.sleep(5)

# -------------------------
# STEP: Success message
# -------------------------

@then("message de succes doit être affiché")
def step_impl(context):
    success = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    assert "compte cree avec succes ! vous pouvez vous connecter." in success.text.lower()
    time.sleep(4)


@step("l’utilisateur doit être redirigé vers /auth/login")
def step_impl(context):
    assert "/auth/login" in context.driver.current_url
    time.sleep(4)


