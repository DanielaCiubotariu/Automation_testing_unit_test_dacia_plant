import unittest
import HTMLTestRunner  # Asigură-te că ai instalat 'htmltestRunner'
from Teste_Login_Dacia_Plant import TestLoginDaciaPlant
from Teste_Butoane_Dacia_Plant import TestButoaneDaciaPlant
from Teste_Produse_Dacia_Plant import TestProduseDaciaPlant
from Teste_newsletter_Dacia_Plant import TestNewsDaciaPlant


class TestSuite(unittest.TestCase):

    def test_suite(self):

        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginDaciaPlant),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestButoaneDaciaPlant),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestProduseDaciaPlant),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestNewsDaciaPlant)
        ])

        runner = HTMLTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='TestReport',
            report_name='Smoke Test Result'
        )

        runner.run(teste_de_rulat)