import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestButoaneDaciaPlant(unittest.TestCase):

    URL = "https://www.daciaplant.ro/"

    # Selectori
    CONTACT_BUTTON_SELECTOR = (By.CSS_SELECTOR, "a[href='/contact'][title='Cum comand']")
    CUM_COMAND_BUTTON_SELECTOR = (By.CSS_SELECTOR, "a[href='/cum-comand'][title='Cum comand']")
    PAGE_TITLE_SELECTOR = (By.CSS_SELECTOR, ".page-title-wrapper h1.page-title span.base")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.URL)
        # Accept cookies if prompted
        try:
            accept_cookies_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-trigger-settings='agree']"))
            )
            accept_cookies_button.click()
        except Exception as e:
            print(f"Exception while accepting cookies: {e}")

    def tearDown(self):
        self.driver.quit()

    def test_contact_page_redirect(self):
        # Identificăm și apăsăm butonul "Contact"
        contact_button = self.driver.find_element(*self.CONTACT_BUTTON_SELECTOR)
        contact_button.click()

        # Așteptăm ca titlul paginii să fie "Contactati-ne"
        try:
            # Așteptăm ca elementul h1 cu clasa page-title să fie vizibil și să conțină textul dorit
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.PAGE_TITLE_SELECTOR)
            )
            page_title = self.driver.find_element(*self.PAGE_TITLE_SELECTOR).text
            expected_title = "CONTACTATI-NE"
            self.assertEqual(page_title, expected_title,
                             f"Titlul paginii nu corespunde. Actual: {page_title}, Așteptat: {expected_title}")
        except Exception as e:
            self.fail(f"Eroare în timpul așteptării titlului paginii: {e}")

    def test_cum_comand_button(self):
        # Click pe butonul "Cum comand?"
        cum_comand_button = self.driver.find_element(*self.CUM_COMAND_BUTTON_SELECTOR)
        cum_comand_button.click()

        # Așteaptă ca pagina să se încarce
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PAGE_TITLE_SELECTOR)
        )

        # Verifică titlul paginii
        page_title = self.driver.find_element(*self.PAGE_TITLE_SELECTOR).text.strip()
        expected_title = "CUM COMAND"
        self.assertEqual(page_title, expected_title,
                         f"Titlul paginii nu corespunde. Actual: '{page_title}', Așteptat: '{expected_title}'")
