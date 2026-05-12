from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

    
def test_login_validation(login_in_driver):
    driver = login_in_driver
    assert "/inventory" in driver.current_url, "No se dirigio al inventario"
    