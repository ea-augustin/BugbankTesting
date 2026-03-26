import time
from behave import when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.credentials import LIBELLE



# -----------------------------
# Ouvrir un compte
# -----------------------------
@then("clique sur le bouton  Ouvrir un compte")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#btn-new-account").click()
    time.sleep(1)


@step("saisit un libellé ou garde celui par défaut")
def step_impl(context):
    label_input = context.driver.find_element(By.CSS_SELECTOR, "[data-testid='input-account-label']")
    label_input.clear()
    label_input.send_keys(LIBELLE)


@then("clique sur le bouton Creer le compte")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-testid='btn-create-account']").click()
    time.sleep(1)


@then("un message de succès doit être affiché")
def step_impl(context):
    success_alert = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='alert-success']"))
    )
    text = success_alert.text.lower()
    assert "succes" in text or "succès" in text, f"Message inattendu : {text}"


@then("un IBAN unique doit être généré")
def step_impl(context):
    ibans = context.driver.find_elements(By.CSS_SELECTOR, "[data-testid^='account-iban']")
    iban_values = [iban.text.strip() for iban in ibans]

    assert len(iban_values) > 0, "Aucun IBAN trouvé sur la page"

    new_iban = iban_values[-1]
    assert new_iban.startswith("FR"), f"IBAN invalide : {new_iban}"


@then("le compte doit être créé avec un solde de 0.00 EUR")
def step_impl(context):
    balances = context.driver.find_elements(By.CSS_SELECTOR, "[data-testid^='account-balance']")
    assert len(balances) > 0, "Aucun solde trouvé sur la page"

    last_balance = balances[-1].text.strip()
    assert last_balance == "0.00 EUR", f"Solde incorrect : {last_balance}"