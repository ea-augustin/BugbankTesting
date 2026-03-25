import time

import behave
import unicodedata
from behave import given, when, then, step, use_step_matcher
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.auth import login
from helpers.credentials import *

use_step_matcher("re")


# -------------------------
# GIVEN: User is logged in
# -------------------------
@given("l’utilisateur est connecté")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    login(context, EMAIL, PASSWORD)

    # Wait for dashboard username to appear
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='username']"))
    )


# -------------------------
# THEN: Redirect to dashboard
# -------------------------
@then("L’utilisateur doit être redirigé vers le tableau de bord.")
def step_impl(context):
    username = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='username']"))
    ).text

    print("Logged in as:", username)
    assert username.lower() == "steve witko"


# -------------------------
# WHEN: Click "mot de passe"
# -------------------------
@when("Clique sur le bouton “mot de passe")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-change-password"))
    ).click()


# -------------------------
# THEN: Redirect to Change Password page
# -------------------------
@then("L’utilisateur doit être redirigé vers le page Changer le mot de passe")
def step_impl(context):
    title = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "changer le mot de passe" in title.text.lower()


# -------------------------
# STEP: Fill password fields
# -------------------------
@step("saisit le mot de passe actuel correct, Nouveau mot de passe et Confirmer le nouveau mot de passe")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-current-password']").send_keys(ACTUALPASS)
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-new-password']").send_keys(UPDATEDPASSWORD)
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-confirm-password']").send_keys(CONFIRMUPDATEDPASSWORD)


# -------------------------
# THEN: Click Save
# -------------------------
@then("Clique sur le bouton Enregistrer")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='btn-change-password']"))
    ).click()



# -------------------------
# THEN: Redirect to dashboard
 # -------------------------
@then("redirigé vers le tableau de bord")
def step_impl(context):
        username = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='username']"))
        ).text

        print("Logged in as:", username)
        assert username.lower() == "steve witko"

        time.sleep(4)

# -------------------------
# STEP: Success message
# -------------------------
@then("message de succès doit être affiché")
def step_impl(context):

    success = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash-messages .alert-success"))
    )
    assert "mot de passe modifie avec succes" in success.text.lower()


