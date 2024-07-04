import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestProduseDaciaPlant(unittest.TestCase):

    URL = "https://www.daciaplant.ro/"

    # Selectori
    LOGIN_BUTTON_SELECTOR = (By.CSS_SELECTOR, "#authorization-trigger")
    EMAIL_INPUT_SELECTOR = (By.ID, "email")
    PASSWORD_INPUT_SELECTOR = (By.ID, "pass")
    LOGIN_SUBMIT_BUTTON_SELECTOR = (By.CSS_SELECTOR, "#send2")
    SEARCH_INPUT_SELECTOR = (By.CSS_SELECTOR, "#search")
    SEARCH_RESULTS_SELECTOR = (By.CSS_SELECTOR, "#toolbar-amount .toolbar-number")
    ADD_TO_CART_SELECTOR = (By.CSS_SELECTOR, ".action.tocart.primary.show-tooltip")
    MINI_CART_COUNTER_SELECTOR = (By.CSS_SELECTOR, "span.counter-number")
    CART_SELECTOR = (By.CSS_SELECTOR, "a.action.showcart")
    DELETE_FROM_CART_BUTTON_SELECTOR = (By.XPATH, "//a[contains(@class, 'action-delete')]")
    PRODUCT_SELECTOR = (By.CSS_SELECTOR, ".product-item-link")
    ADD_TO_WISHLIST_SELECTOR = (By.CSS_SELECTOR, "a.action.towishlist")

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

    def test_search(self):
        # Introducem "Calmotusin" în câmpul de căutare
        search_input = self.driver.find_element(*self.SEARCH_INPUT_SELECTOR)
        search_input.send_keys("Calmotusin")

        # Apăsăm Enter pentru a efectua căutarea
        search_input.submit()

        try:
            # Așteptăm să se încarce rezultatele căutării
            search_results = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SEARCH_RESULTS_SELECTOR)
            ).text
            # Convertim textul rezultatului într-un număr
            num_results = int(search_results.split()[0])
            self.assertGreater(num_results, 0, "Numărul rezultatelor căutării pentru Calmotusin nu este mai mare de 0")
        except Exception as e:
            self.fail(f"Nu s-a găsit sau nu a fost afișat numărul rezultatelor căutării pentru Calmotusin: {e}")

    def test_add_to_cart(self):
        try:
            # Căutăm "Biseptol Spray Propolis" în câmpul de căutare
            search_input = self.driver.find_element(*self.SEARCH_INPUT_SELECTOR)
            search_input.send_keys("Biseptol Spray Propolis")
            search_input.submit()

            # Așteptăm să se încarce rezultatele căutării și să fie vizibile
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ADD_TO_CART_SELECTOR)
            )

            # Apăsăm pe butonul de adăugare în coș
            add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_SELECTOR)
            add_to_cart_button.click()

            # Așteptăm 2 secunde pentru ca numărul din mini coș să se actualizeze
            time.sleep(2)

            # Verificăm dacă numărul din mini coș este cel puțin 2 pentru ca se adauga automat si un produs cadou
            mini_cart_count = int(self.driver.find_element(*self.MINI_CART_COUNTER_SELECTOR).text)
            self.assertGreaterEqual(
                mini_cart_count, 2,
                f"Expected mini cart count to be at least 2, but found {mini_cart_count}"
            )

        except Exception as e:
            print(f"Exception occurred: {e}")
            self.fail(f"Nu s-a putut adăuga produsul în coș sau nu a apărut mesajul corespunzător")

    def test_add_and_remove_from_cart(self):
        try:
            # Căutăm "Calmotusin comprimate" în câmpul de căutare
            search_input = self.driver.find_element(*self.SEARCH_INPUT_SELECTOR)
            search_input.send_keys("Calmotusin comprimate")
            search_input.submit()

            # Așteptăm să se încarce rezultatele căutării și să fie vizibile
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ADD_TO_CART_SELECTOR)
            )

            # Apăsăm pe butonul de adăugare în coș
            add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_SELECTOR)
            add_to_cart_button.click()

            # Așteptăm 2 secunde pentru ca numărul din mini coș să se actualizeze
            time.sleep(2)

            # Apăsăm pe butonul de coș
            cart_button = self.driver.find_element(*self.CART_SELECTOR)
            cart_button.click()

            # Așteptăm să se încarce pagina coșului de cumpărături
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart.item"))
            )

            # Găsim link-ul pentru ștergerea produsului din coș
            delete_button = self.driver.find_element(*self.DELETE_FROM_CART_BUTTON_SELECTOR)
            delete_button.click()

            # Așteptăm 2 secunde pentru ca numărul din mini coș să se actualizeze din nou
            time.sleep(2)

            # Verificăm dacă numărul din mini coș este cel puțin 1
            mini_cart_count = int(self.driver.find_element(*self.MINI_CART_COUNTER_SELECTOR).text)
            self.assertGreaterEqual(
                mini_cart_count, 1,
                f"Expected mini cart count to be at least 1, but found {mini_cart_count}"
            )

        except Exception as e:
            print(f"Exception occurred: {e}")
            self.fail(f"Nu s-a putut adăuga sau șterge produsul din coș sau nu a apărut mesajul corespunzător")

    def test_add_to_wishlist(self):
        # Login with valid credentials
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR)
        login_button.click()

        email_input = self.driver.find_element(*self.EMAIL_INPUT_SELECTOR)
        email_input.send_keys("teste.automate@yahoo.com")

        password_input = self.driver.find_element(*self.PASSWORD_INPUT_SELECTOR)
        password_input.send_keys("TesteAutomate")

        login_submit_button = self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON_SELECTOR)
        login_submit_button.click()

        # Wait for login to complete
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.daciaplant.ro/customer/account/"))

        # Search for "Belène Collagen beauty drink 28buc"
        search_input = self.driver.find_element(*self.SEARCH_INPUT_SELECTOR)
        search_input.send_keys("Belène Collagen beauty drink 28buc")
        search_input.submit()

        # Wait for search results to load
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//strong[contains(@class, 'product-item-name')]/a[contains(@class, 'product-item-link')]"))
        )

        # Click on the product link
        product_link = self.driver.find_element(*self.PRODUCT_SELECTOR)
        product_link.click()

        # Wait for the product page to load
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.action.towishlist"))
        )

        # Click on "Add to wishlist" button
        add_to_wishlist_button = self.driver.find_element(*self.ADD_TO_WISHLIST_SELECTOR)
        add_to_wishlist_button.click()

        # Wait for redirection to wishlist page
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://www.daciaplant.ro/wishlist/index/index/wishlist_id/24241/")
        )

        # Assert that the current URL is the wishlist page
        self.assertEqual(self.driver.current_url, "https://www.daciaplant.ro/wishlist/index/index/wishlist_id/24241/")
