import pytest
from selenium import webdriver
from utils.loginPage import login

@pytest.fixture  #configuracion que se inserta en diferentes pruebas
def driver():  # contiene la inicializacion de las pruebas
     options = webdriver.ChromeOptions()
     options.add_argument("--incongnito")
     
     driver = webdriver.Chrome(options= options)
     
     yield driver 
     driver.quit()

@pytest.fixture
def login_in_driver(driver):
     login(driver)
     return driver