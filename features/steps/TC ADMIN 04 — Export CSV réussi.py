import os
import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.credentials import ADMIN_EMAIL, ADMIN_PASSWORD


DOWNLOAD_DIR = r"D:\ENI - Testeur\Stage\csv"
CSV_FILE = os.path.join(DOWNLOAD_DIR, "users_export.csv")


@given("l’utilisateur est un admin")
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


@when("l’utilisateur se rend sur /admin/export/users")
def step_impl(context):
    context.driver.get(context.base_url + "/admin/")
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-export"))
    )


@then("tous les utilisateurs doivent être récupérés")
def step_impl(context):
    # Vérifie que le bouton export est présent
    export_btn = context.driver.find_element(By.CSS_SELECTOR, "#btn-export")
    assert export_btn.is_displayed(), "Le bouton d'export n'est pas visible"


@then("un fichier CSV doit être généré")
def step_impl(context):
    # Clique sur le bouton d’export
    context.driver.find_element(By.CSS_SELECTOR, "#btn-export").click()

    # Attendre un peu que le téléchargement démarre
    time.sleep(2)


@then("le fichier users_export.csv doit être téléchargé")
def step_impl(context):
    # Attendre jusqu'à 10 secondes que le fichier apparaisse
    for _ in range(10):
        if os.path.exists(CSV_FILE):
            break
        time.sleep(1)

    assert os.path.exists(CSV_FILE), (
        f"Le fichier users_export.csv n'a pas été trouvé dans : {DOWNLOAD_DIR}"
    )
