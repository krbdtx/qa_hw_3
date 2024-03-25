import pytest
from selene import browser


@pytest.fixture()
def setting_browser():
    browser.config.window_height = 480
    browser.config.window_width = 640
    yield
    browser.quit()

@pytest.fixture()
def skip():
    """""
    TODO: добавить передачу  искомой переменной в вывод
    """""
    return pytest.skip("Ошибка, не находит")