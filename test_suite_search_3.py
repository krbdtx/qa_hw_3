from selene import browser, be, have

search_txt = 'yashaka/selene'
search_txt_in_brow = 'User-oriented Web UI browser tests in Python. Contribute to '

def test_01(setting_browser):
    ''''
        Проверка поиска строки Гуглом
        Успешно найдено
    '''
    
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(search_txt).press_enter()
    browser.element('[id="search"]').should(have.text(search_txt_in_brow))


def test_02(skip):
    ''''
        Проверка поиска строки Рамблером
        Успешно не найдено
    '''

    browser.open('https://rambler.ru')
    browser.element('[placeholder="Поиск по интернету"]').should(be.blank).type(search_txt).press_enter()
    browser.element('[class="serp-item serp-item_card "]')\
        .should(have.text(search_txt_in_brow))


def test_03(setting_browser):
    ''''
        Проверка поиска строки Яндексом
        Успешно найдено
    '''

    browser.open('https://ya.ru')
    browser.element('[aria-label="Запрос"]').should(be.blank).type(search_txt).press_enter()
    browser.element('[class="serp-item serp-item_card "]')\
        .should(have.text(search_txt_in_brow))
