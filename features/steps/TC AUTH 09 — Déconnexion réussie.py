import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.auth import login
from helpers.credentials import EMAIL, PASSWORD


@given("l’utilisateur est déjà connecté")
def step_impl(context):
    # Create the driver BEFORE calling login()
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    login(context, EMAIL, PASSWORD)
    time.sleep(2)


@when("l’utilisateur clique sur le bouton de déconnexion")
def step_impl(context):
    context.driver.find_element(By.ID, "nav-logout").click()
    time.sleep(2)


@then("l’utilisateur doit être redirigé vers la page de connexion")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    # URL check
    wait.until(EC.url_contains("/auth/login"))

    # Logout confirmation message
    logout_message = context.driver.find_element(
        By.XPATH, "//*[contains(text(), 'Vous avez ete deconnecte')]"
    ).text

    assert "Vous avez ete deconnecte" in logout_message