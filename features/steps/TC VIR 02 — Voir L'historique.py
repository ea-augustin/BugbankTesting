from behave import when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then("clique sur le bouton historique")
def step_impl(context):
    # The history button is the navbar link:
    # <a href="/transfer/history" id="nav-history">
    history_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-history"))
    )
    history_btn.click()


@then("l’utilisateur voir l'historique")
def step_impl(context):
    # The history page contains a table with:
    # <div class="table-wrapper" data-testid="history-table">
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='history-table']"))
    )

    # Optional: verify at least one row exists
    rows = context.driver.find_elements(By.CSS_SELECTOR, "[data-testid^='history-row']")
    assert len(rows) > 0, "Aucune ligne d'historique trouvée"