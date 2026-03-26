from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.credentials import ADMIN_EMAIL, ADMIN_PASSWORD


@given("l'utilisateur est connecté en rôle admin")
def step_impl(context):
    context.driver.get(context.base_url + "/auth/login")

    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='input-email']"))
    ).send_keys(ADMIN_EMAIL)

    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-password']").send_keys(ADMIN_PASSWORD)
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='btn-login']").click()

    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#nav-admin"))
    )


@when("l'utilisateur click sur btn admin")
def step_impl(context):
    admin_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-admin"))
    )
    admin_btn.click()


@when("l'utilisateur se rend sur la page /admin/")
def step_impl(context):
    context.driver.get(context.base_url + "/admin/")
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='admin-users-table']"))
    )


@then("la liste de tous les utilisateurs doit être affichée")
def step_impl(context):
    user_table = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='admin-users-table']"))
    )
    assert user_table.is_displayed(), "La table des utilisateurs n’est pas visible"


@then("les statistiques globales doivent être affichées")
def step_impl(context):
    selectors = [
        "[data-testid='stat-users']",
        "[data-testid='stat-accounts']"
    ]

    for selector in selectors:
        stat = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
        )
        value = stat.text.strip()
        assert value.isdigit(), f"Statistique invalide ou absente : {value}"