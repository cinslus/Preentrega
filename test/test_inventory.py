from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver

def test_inventory_title(driver_logged):
    title = driver_logged.title
    titulo_esperado = "Swag Labs"
    
    assert title == titulo_esperado, f"Error: El título esperado era '{titulo_esperado}', pero se obtuvo '{title}'"
    

def test_productos_visibles(driver_logged):
    productos = driver_logged.find_elements(By.CLASS_NAME,"inventory_item")
    
    assert len(productos) > 0, "Error: No se encontraron productos en la página."

def test_ui_elements(driver_logged):
    try:
        menu = driver_logged.find_element(By.ID, "react-burger-menu-btn")
        filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")
        carrito = driver_logged.find_element(By.ID, "shopping_cart_container")
        subtitulo = driver_logged.find_element(By.CLASS_NAME, "header_secondary_container")

    # Evalua si esta visible en la pagina
        assert menu.is_displayed(), "El icono del menu no está presente en la pagina" 
        assert filtro.is_displayed(), "El filtro del catalogo no está presente en la pagina"
        assert carrito.is_displayed(), "El carrito no se encuentra presente en la pagina"
        assert subtitulo.is_displayed(), "La pagina no contiene subtitulo"
    #captura el error del test
    except Exception as e:
            print(f"Error en test_ui_elements: {e}")
            raise