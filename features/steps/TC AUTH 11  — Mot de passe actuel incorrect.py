import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.auth import login
from helpers.credentials import (
    EMAIL,
    PASSWORD,
    UPDATEDPASSWORD,
    CONFIRMUPDATEDPASSWORD
)


# -------------------------
# GIVEN: User is logged in
# -------------------------
@given("l'utilisateur est connecté")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    login(context, EMAIL, PASSWORD)

    # Wait for dashboard to load
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='username']"))
    )


# -------------------------
# WHEN: Click "mot de passe" in navbar
# -------------------------
@when("Clique sur le bouton mot de passe")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-change-password"))
    ).click()

    # Verify page loaded
    title = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "changer le mot de passe" in title.text.lower()


# -------------------------
# WHEN: Wrong current password
# -------------------------
@when("saisit un mot de passe actuel incorrect")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-current-password']").send_keys("WrongPass123!")
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-new-password']").send_keys(UPDATEDPASSWORD)
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-confirm-password']").send_keys(CONFIRMUPDATEDPASSWORD)


# -------------------------
# WHEN: Submit form
# -------------------------
@when("soumet")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='btn-change-password']"))
    ).click()


# -------------------------
# THEN: Error message must appear
# -------------------------
@then("un message d'erreur doit être affiché")
def step_impl(context):
    error = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash-messages .alert-danger"))
    )
    assert "mot de passe actuel incorrect" in error.text.lower()


# -------------------------
# THEN: No change must be saved
# -------------------------
@then("aucun changement ne doit être sauvegardé")
def step_impl(context):
    # User must remain on the same page
    assert "/auth/change-password" in context.driver.current_url.lower()