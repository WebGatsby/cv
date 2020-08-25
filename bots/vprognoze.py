import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import datetime
import re


# open browser
def open_browser():
    fp = webdriver.FirefoxProfile('\\firefox_profile')
    options = Options()
    options.headless = False
    browser = webdriver.Firefox(fp, options=options)
    return browser


# get bets info
def get_bet_info(browser, last_bet_id):
    bets_to_place = []
    i = 0
    browser.get('https://vprognoze.ru/lenta/')
    time.sleep(20)
    page_source = browser.page_source
    soup1 = BeautifulSoup(page_source, 'html.parser')
    tips = soup1.find_all('tr', {'class': 'tab_pad'})
    while tips[i].attrs.get('id') != last_bet_id:
        date_temp = tips[i].find_all('td', {'class': ''})[1].text
        sport = tips[i].find('span', {'class': 'span-title'}).text
        players = tips[i].find_all('a', {'class': ''})[2].text
        bet = tips[i].find('span', {'class': ''}).text
        bets_to_place.append([date_temp, sport, players, bet])
        i += 1
    else:
        last_bet_id = tips[0].attrs.get('id')

    return bets_to_place, last_bet_id

