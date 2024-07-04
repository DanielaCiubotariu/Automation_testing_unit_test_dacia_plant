import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNewsDaciaPlant(unittest.TestCase):

    URL = "https://www.daciaplant.ro/"

    #Selectori
    NEWSLETTER_NAME_SELECTOR = (By.ID, "mce-LNAME")
    NEWSLETTER_EMAIL_SELECTOR = (By.ID, "newsletter")
    NEWSLETTER_SUBSCRIBE_BUTTON_SELECTOR = (By.ID, "mc-embedded-subscribe")
    NEWSLETTER_ERROR_MESSAGE_SELECTOR = (By.ID, "newsletter-error")
    NEWSLETTER_SUCCESS_MESSAGE_SELECTOR = ( By.XPATH, "//div[contains(@class, 'mf-initial') and contains(text(), 'Solicitarea de confirmare a fost trimisa.')]")

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

    def test_newsletter_subscription_invalid_email(self):
        # Introducem numele pentru newsletter (nu este necesar pentru acest test)
        name_input = self.driver.find_element(*self.NEWSLETTER_NAME_SELECTOR)
        name_input.send_keys("John Doe")  # Exemplu de nume

        # Introducem o adresă de email invalidă
        email_input = self.driver.find_element(*self.NEWSLETTER_EMAIL_SELECTOR)
        email_input.send_keys("invalid_email")

        # Apăsăm butonul de abonare la newsletter
        subscribe_button = self.driver.find_element(*self.NEWSLETTER_SUBSCRIBE_BUTTON_SELECTOR)
        subscribe_button.click()

        try:
            # Așteptăm să apară mesajul de eroare
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.NEWSLETTER_ERROR_MESSAGE_SELECTOR)
            ).text
            expected_message = "Introduceti o adresa email validas (Ex: johndoe@domain.com)."
            self.assertEqual(error_message, expected_message,
                             f"Mesajul de eroare nu corespunde. Actual: '{error_message}', Așteptat: '{expected_message}'")
        except Exception as e:
            self.fail(f"Nu s-a găsit sau nu a fost afișat mesajul de eroare pentru email invalid: {e}")

    def test_newsletter_subscription_valid_email(self):
        # Introducem numele pentru newsletter
        name_input = self.driver.find_element(*self.NEWSLETTER_NAME_SELECTOR)
        name_input.send_keys("Teste")

        # Introducem o adresă de email validă
        email_input = self.driver.find_element(*self.NEWSLETTER_EMAIL_SELECTOR)
        email_input.send_keys("teste.automate@yahoo.com")

        # Apăsăm butonul de abonare la newsletter
        subscribe_button = self.driver.find_element(*self.NEWSLETTER_SUBSCRIBE_BUTTON_SELECTOR)
        subscribe_button.click()

        try:
            # Așteptăm să apară mesajul de confirmare
            success_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.NEWSLETTER_SUCCESS_MESSAGE_SELECTOR)
            ).text
            expected_message = "Solicitarea de confirmare a fost trimisa."
            self.assertEqual(success_message, expected_message,
                             f"Mesajul de succes nu corespunde. Actual: '{success_message}', Așteptat: '{expected_message}'")
        except Exception as e:
            self.fail(f"Nu s-a găsit sau nu a fost afișat mesajul de confirmare: {e}")
