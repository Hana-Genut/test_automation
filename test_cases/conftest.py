import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from python_automation.utilities.manage_pages import Page_Manager
from python_automation.utilities.read_properties import get_data

driver = None


@pytest.fixture(scope='class')
def init_web(request):
    browser_type = get_data("Browser")
    if browser_type == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        driver = None
        print("Wrong input, unrecognized browser")

    globals()['driver'] = driver
    request.cls.driver = driver
    driver.maximize_window()

    Page_Manager.init_web_page(driver)

    yield
    driver.quit()

