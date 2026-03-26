from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Dossier où Chrome doit télécharger les fichiers
    prefs = {
        "download.default_directory": r"D:\ENI - Testeur\Stage\csv",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Lancement du navigateur
    context.driver = webdriver.Chrome(options=chrome_options)

    # URL de base de l'application
    context.base_url = "https://testapp.campus-eni.fr"


def after_all(context):
    context.driver.quit()