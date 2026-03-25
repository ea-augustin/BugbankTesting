import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from helpers.credentials import URLLOGIN, EMAIL, PASSWORD


@given("l’utilisateur est sur la page de connexion")
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.driver.get(URLLOGIN)


@when("l’utilisateur saisit un email valide 'steve@bugbank.fr' et un mot de passe valide 'T9m#Q4v!Rp'")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-email']").send_keys(EMAIL)
    context.driver.find_element(By.XPATH, "//*[@data-testid='input-password']").send_keys(PASSWORD)


@then("clique sur le bouton de connexion")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='btn-login']").click()


@then("l’utilisateur doit être redirigé vers le tableau de bord")
def step_impl(context):
    username = context.driver.find_element(By.CSS_SELECTOR, "[data-testid='username']").text
    print("Logged in as:", username)
    assert username.lower() == "steve witko"

    time.sleep(2)