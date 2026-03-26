from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.auth import login
from helpers.credentials import EMAIL, PASSWORD, UPDATEDPASSWORD


@given("utilisateur est connecte")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    login(context, EMAIL, PASSWORD)

    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='username']"))
    )


@when("Clique sur le bouton mot de passe")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-change-password"))
    ).click()

    title = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "changer le mot de passe" in title.text.lower()


@when("soumet")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='btn-change-password']"))
    ).click()


@when("saisit un nouveau mot de passe")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-new-password']").send_keys(UPDATEDPASSWORD)


@then("aucun changement ne doit être sauvegardé")
def step_impl(context):
    assert "/auth/change-password" in context.driver.current_url.lower()