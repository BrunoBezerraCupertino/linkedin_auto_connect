import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from login import email, senha


email = email
senha = senha
driver = webdriver.Chrome()


class AutoLinkedin:
    def login(self):
        driver.get(r'https://www.linkedin.com/login/pt')
        driver.find_element_by_id('username').send_keys(email)
        driver.find_element_by_id('password').send_keys(senha + Keys.RETURN)

    def pesquisar(self, pesquisa):
        driver.find_element_by_css_selector('#global-nav-typeahead > input').send_keys(pesquisa + Keys.RETURN)
        time.sleep(5)
        driver.find_element_by_css_selector('#search-reusables__filters-bar > ul > li:nth-child(5) > button').click()


if __name__ == '__main__':
    chrome = AutoLinkedin()
    chrome.login()
    chrome.pesquisar('python')


