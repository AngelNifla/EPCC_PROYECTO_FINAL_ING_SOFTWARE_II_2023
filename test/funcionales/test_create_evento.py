import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import service as ChromeService
import time

class test_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_create_evento(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        title : driver.title
        self.assertIn("Sistema de Publicación de Eventos", driver.title)

        #driver.maximize_window()
        math_calc = driver.find_element(by=By.XPATH, value="//*[@id='navbarResponsive']/ul/li[2]/a")
        math_calc.click()
        #driver.implicitly_wait(10)

        # Enter value 10 in the first number of the percent Calculator
        first_text = driver.find_element(by=By.XPATH, value="//*[@id='typeEmailX']")
        
        first_text.send_keys("LeviC@gmail.com")
        # Enter value 50 in the second number of the percent Calculator

        second_text = driver.find_element(by=By.XPATH, value="//*[@id='typePasswordX']")
        second_text.send_keys("Levi")

        #Click  Button
        button = driver.find_element(by=By.XPATH, value="//*[@id='content']/input")
        button.click()
        
        # implicit wait
        # driver.implicitly_wait(10)
        
        button = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div/a")
        button.click()

        nombre = driver.find_element(by=By.XPATH, value='//*[@id="evento_nombre"]')
        nombre.send_keys("Ejemplo")

        detalles = driver.find_element(by=By.XPATH, value='//*[@id="evento_detalles"]')
        detalles.send_keys("Detalles ejemplo")

        enlace = driver.find_element(by=By.XPATH, value='//*[@id="evento_link"]')
        enlace.send_keys("Link")

        button = driver.find_element(by=By.XPATH, value='//*[@id="button_create"]')
        button.click()

        nombre_evento = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[11]/a/h2')
        self.assertEqual(nombre_evento.text,"Ejemplo")

        detalles_evento = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[11]/a/h3')
        self.assertEqual(detalles_evento.text,"Detalles ejemplo")

        

    def tearDown(self):
        # Close the Browser.
        self.driver.close()

if __name__ == "__main__":
    unittest.main()