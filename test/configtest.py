import pytest
from selenium import webdriver

from config.config import TestData


@pytest.fixture(params=["Chrome"], scope='class')
def init_driver(request):
    if request.param == "Chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.chrome_Executable_Path)
    request.cls.driver = web_driver
    yield
    web_driver.close()
