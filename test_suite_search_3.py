from selene import browser, be, have
import pytest

search_txt = 'yashaka/selene'
search_txt_error = 'фывфывфывфыввайцйц'
search_txt_in_brow = 'User-oriented Web UI browser tests in Python. Contribute to '
search_txt_in_error = 'По введённому запросу ничего не найдено'

def test_01(setting_browser):
    ''''
        Проверка поиска строки Гуглом
        Успешно найдено
    '''
    
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(search_txt).press_enter()
    browser.element('[id="search"]').should(have.text(search_txt_in_brow))


def test_02():
    ''''
        Проверка поиска строки Рамблером
        Успешно не найдено
    '''

    browser.open('https://rambler.ru')
    browser.element('[placeholder="Поиск по интернету"]').should(be.blank).type(search_txt_error).press_enter()
    browser.element('[class="Error__title--3qsmL"]').should(have.text(search_txt_in_error))


def test_03(setting_browser):
    ''''
        Проверка поиска строки Яндексом
        Успешно найдено
    '''

    browser.open('https://ya.ru')
    browser.element('[aria-label="Запрос"]').should(be.blank).type(search_txt).press_enter()
    browser.element('[class="serp-item serp-item_card "]')\
        .should(have.text(search_txt_in_brow))
