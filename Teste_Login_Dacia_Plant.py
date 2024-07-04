import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestLoginDaciaPlant(unittest.TestCase):

    URL = "https://www.daciaplant.ro/"

    # Selectori
    LOGIN_BUTTON_SELECTOR = (By.CSS_SELECTOR, "#authorization-trigger")
    EMAIL_INPUT_SELECTOR = (By.ID, "email")
    PASSWORD_INPUT_SELECTOR = (By.ID, "pass")
    LOGIN_SUBMIT_BUTTON_SELECTOR = (By.CSS_SELECTOR, "#send2")
    ERROR_MESSAGE_SELECTOR = (By.XPATH, "//div[@data-ui-id='message-error']")
    LOGOUT_BUTTON_SELECTOR = (By.CSS_SELECTOR, "#authorization-trigger")
    LOGOUT_SUBMIT_BUTTON_SELECTOR = (By.XPATH, "//a[@href='https://www.daciaplant.ro/customer/account/logout/']")

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

    def test_login_invalid_credentials(self):
        # Click pe butonul de conectare
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR)
        login_button.click()

        # Introducem email invalid
        email_input = self.driver.find_element(*self.EMAIL_INPUT_SELECTOR)
        email_input.send_keys("invalid@email.com")

        # Introducem parola invalida
        password_input = self.driver.find_element(*self.PASSWORD_INPUT_SELECTOR)
        password_input.send_keys("invalidpassword")

        # Apasam butonul de submit pentru conectare
        login_submit_button = self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON_SELECTOR)
        login_submit_button.click()

        try:
            # Asteptam ca mesajul de eroare sa fie vizibil
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE_SELECTOR)
            ).text
            self.assertIn(
                "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.",
                error_message,
                "Expected error message not found"
            )
        except TimeoutException:
            self.fail("Error message not found or not visible")

    def test_login_valid_credentials(self):
        # Click pe butonul de conectare
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR)
        login_button.click()

        # Introducem emailul
        email_input = self.driver.find_element(*self.EMAIL_INPUT_SELECTOR)
        email_input.send_keys("teste.automate@yahoo.com")

        # Introducem parola
        password_input = self.driver.find_element(*self.PASSWORD_INPUT_SELECTOR)
        password_input.send_keys("TesteAutomate")

        # Apăsăm butonul de submit pentru conectare
        login_submit_button = self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON_SELECTOR)
        login_submit_button.click()

        # Așteptăm ca pagina să se încarce după autentificare
        self.driver.implicitly_wait(10)

        # Verificăm dacă suntem redirecționați pe pagina corectă
        expected_url = "https://www.daciaplant.ro/customer/account/"
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url,
                         f"URL-ul curent nu corespunde celui așteptat. Actual: {current_url}, Așteptat: {expected_url}")

    def test_login_and_logout(self):
        # Click pe butonul de conectare
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR)
        login_button.click()

        # Introducem emailul și parola valide
        email_input = self.driver.find_element(*self.EMAIL_INPUT_SELECTOR)
        email_input.send_keys("teste.automate@yahoo.com")

        password_input = self.driver.find_element(*self.PASSWORD_INPUT_SELECTOR)
        password_input.send_keys("TesteAutomate")

        # Apăsăm butonul de submit pentru conectare
        login_submit_button = self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON_SELECTOR)
        login_submit_button.click()

        try:
            # Așteptăm ca butonul de logout să fie vizibil
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.LOGOUT_BUTTON_SELECTOR)
            )

            # Verificăm că butonul de logout este prezent, indicând o conectare reușită
            self.assertTrue(self.driver.find_element(*self.LOGOUT_BUTTON_SELECTOR).is_displayed())

            # Click pe butonul de logout
            logout_button = self.driver.find_element(*self.LOGOUT_BUTTON_SELECTOR)
            logout_button.click()

            # Așteptăm ca butonul de submit pentru logout să fie vizibil și apoi facem click pe el
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.LOGOUT_SUBMIT_BUTTON_SELECTOR)
            ).click()

            # Așteptăm câteva secunde pentru ca delogarea să se finalizeze
            self.driver.implicitly_wait(5)

            # Verificăm dacă suntem redirectionati pe pagina de delogare
            expected_url = "https://www.daciaplant.ro/customer/account/logoutSuccess/"
            current_url = self.driver.current_url
            self.assertEqual(current_url, expected_url,
                             f"URL-ul curent nu corespunde celui așteptat după delogare. Actual: {current_url}, Așteptat: {expected_url}")

        except TimeoutException:
            self.fail("Butonul de logout sau butonul de submit pentru logout nu au fost găsite sau nu au fost accesibile")
