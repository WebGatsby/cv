import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import csv
import datetime


def find_match_in_oddsfan(browser, bet_to_place):
    check = 5
    browser.get('https://www.oddsfan.ru/')
    time.sleep(5)

    # change timezone
    change_timezone = browser.find_element_by_class_name("drop-open")
    change_timezone.click()
    my_timezone = browser.find_element_by_partial_link_text('GMT+05:00')
    my_timezone.click()
    time.sleep(10)

    possible_events = [0]
    time_to_go = False

    # find event by words in head of match
    for words in range(0, len(bet_to_place[2].split(' '))):
        search_results = 0
        while search_results < len(possible_events):
            browser.get('https://www.oddsfan.ru/')
            search_bar = browser.find_element_by_class_name("select2-search__field")
            search_bar.send_keys(bet_to_place[2].split(' ')[words])
            time.sleep(3)
            possible_events = browser.find_elements_by_class_name("select2-results__option")
            try:
                possible_events[search_results].click()
                time.sleep(20)
                odds_date = browser.find_element_by_class_name('date').text.split(' ')
                if odds_date[1] == bet_to_place[0][:2] and odds_date[-1] == bet_to_place[0][5:]:
                    time_to_go = True
                    break
            except Exception:
                odds_date = ['0', '0']
            search_results += 1

        if time_to_go:
            break

    # get link to Pinnacle
    page = BeautifulSoup(browser.page_source, 'html.parser')
    outcome_kefs = page.find_all('div', {'class': 'collapse'})
    links = page.find_all('span', {'class': 'number'})
    names = page.find_all('a', {'data-toggle': "collapse"})

    for i in range(1, len(outcome_kefs)):
        if outcome_kefs[i].text.find("Pinnacle") != -1:
            if names[2].text.find('Победитель') == -1:
                f3 = 'https://www.oddsfan.ru' + links[i*3].contents[1].attrs['href']
            else:
                f3 = 'https://www.oddsfan.ru' + links[i*2].contents[1].attrs['href']
            time.sleep(5)
            browser.get(f3)
            time.sleep(5)
            browser.get(f3)
            time.sleep(5)
            browser.get(browser.current_url.replace('ru', 'en'))
            time.sleep(5)
            check = 0
            break
    if check != 0:
        return -1




