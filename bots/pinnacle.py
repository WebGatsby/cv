import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re
import csv


# find bet in Pinnacle page (yes, its the easiest way)
def find_pinnacle_way(bet_to_place, pinnacle_bets):
    bet_type = bet_to_place[3].split(' ')[0]
    bet_numbers = re.findall(r'\(.*?\)', bet_to_place[3])

    if len(bet_numbers) == 0:
        return [0, 0, -1]
    pinnacle_bet_list = [0, 0, -1]

    if bet_type == 'П1':
        pinnacle_bet_list[0] = 'Money Line – Match'
        pinnacle_bet_list[1] = pinnacle_bets[0][1]
        pinnacle_bet_list[2] = 1

    if bet_type == 'П2':
        pinnacle_bet_list[0] = 'Money Line – Match'
        pinnacle_bet_list[1] = pinnacle_bets[0][-3]
        pinnacle_bet_list[2] = 0

    if bet_type == 'ТБ':
        pinnacle_bet_list[0] = 'Total – Match'
        pinnacle_bet_list[1] = 'Over ' + bet_numbers[0].replace(')', '').replace('(', '')

    if bet_type == 'ТМ':
        pinnacle_bet_list[0] = 'Total – Match'
        pinnacle_bet_list[1] = 'Under ' + bet_numbers[0].replace(')', '').replace('(', '')

    if bet_type == 'ФОРА1':
        pinnacle_bet_list[0] = 'Handicap – Match'
        pinnacle_bet_list[1] = bet_numbers[0].replace(')', '').replace('(', '')
        pinnacle_bet_list[2] = 1

    if bet_type == 'ФОРА2':
        pinnacle_bet_list[0] = 'Handicap – Match'
        pinnacle_bet_list[1] = bet_numbers[0].replace(')', '').replace('(', '')
        pinnacle_bet_list[2] = 0

    if bet_type == 'ИТБ1':
        pinnacle_bet_list[0] = 'Team Total – Match'
        pinnacle_bet_list[1] = 'Over ' + bet_numbers[0].replace(')', '').replace('(', '')
        pinnacle_bet_list[2] = 1

    if bet_type == 'ИТБ2':
        pinnacle_bet_list[0] = 'Team Total – Match'
        pinnacle_bet_list[1] = 'Over ' + bet_numbers[0].replace(')', '').replace('(', '')
        pinnacle_bet_list[2] = 0

    if bet_type == 'ИТМ1':
        pinnacle_bet_list[0] = 'Team Total – Match'
        pinnacle_bet_list[1] = 'Under ' + bet_numbers[0].replace(')', '').replace('(', '')
        pinnacle_bet_list[2] = 1

    if bet_type == 'ИТМ2':
        pinnacle_bet_list[0] = 'Team Total – Match'
        pinnacle_bet_list[1] = 'Under ' + bet_numbers[0].replace(')', '').replace('(', '')
        pinnacle_bet_list[2] = 0

    if bet_type == 'Обе команды забьют: Нет':
        pinnacle_bet_list[0] = 'Both Teams To Score'
        pinnacle_bet_list[1] = 'No'

    if bet_type == 'Обе команды забьют: Да':
        pinnacle_bet_list[0] = 'Both Teams To Score'
        pinnacle_bet_list[1] = 'Yes'

    if bet_to_place[3].find('ФОРА1 по геймам') != -1:
        pinnacle_bet_list[0] = 'Handicap – Match'
        pinnacle_bet_list[1] = bet_numbers[0].replace(')', '').replace('(', '')
        pinnacle_bet_list[2] = 1

    if bet_to_place[3].find('ФОРА2 по геймам') != -1:
        pinnacle_bet_list[0] = 'Handicap – Match'
        pinnacle_bet_list[1] = bet_numbers[0].replace(')', '').replace('(', '')
        pinnacle_bet_list[2] = 0

    if bet_to_place[3].find('Тотал по геймам больше') != -1:
        pinnacle_bet_list[0] = 'Total – Match'
        pinnacle_bet_list[1] = 'Over ' + bet_numbers[0].replace(')', '').replace('(', '')

    if bet_to_place[3].find('Тотал по геймам меньше') != -1:
        pinnacle_bet_list[0] = 'Total – Match'
        pinnacle_bet_list[1] = 'Under ' + bet_numbers[0].replace(')', '').replace('(', '')

    if bet_to_place[3].find('1-й сет П1') != -1:
        pinnacle_bet_list[0] = 'Money Line – 1st Set'
        pinnacle_bet_list[1] = pinnacle_bets[0][1]
        pinnacle_bet_list[2] = 1

    if bet_to_place[3].find('1-й сет П2') != -1:
        pinnacle_bet_list[0] = 'Money Line – 1st Set'
        pinnacle_bet_list[1] = pinnacle_bets[0][-3]
        pinnacle_bet_list[2] = 0

    if bet_to_place[3].find('ФОРА1 по сетам') != -1:
        pinnacle_bet_list[0] = 'Set Markets'
        pinnacle_bet_list[1] = pinnacle_bets[0][1] + '(' + bet_numbers[0].replace(')', '').replace('(', '') + 'Sets)'
        pinnacle_bet_list[2] = 1

    if bet_to_place[3].find('ФОРА2 по сетам') != -1:
        pinnacle_bet_list[0] = 'Set Markets'
        pinnacle_bet_list[1] = pinnacle_bets[0][-3] + '(' + bet_numbers[0].replace(')', '').replace('(', '') + 'Sets)'
        pinnacle_bet_list[2] = 0

    return pinnacle_bet_list


# place bet, input money amount and confirm bet
def place_bet(browser, pinnacle_bets, pinnacle_bet_list):
    bet_number = 9999
    for bet_types in range(0, len(pinnacle_bets)):
        if pinnacle_bet_list[0] == pinnacle_bets[bet_types][0]:
            for bet in range(1, len(pinnacle_bets[bet_types]), 3):
                if pinnacle_bet_list[1] == pinnacle_bets[bet_types][bet] and bet % 2 == pinnacle_bet_list[2]:
                    bet_number = pinnacle_bets[bet_types][bet+2]
                    break
    kefs = browser.find_elements_by_class_name('label')
    kefs[bet_number].click()
    time.sleep(5)
    placeForMoney = browser.find_elements_by_tag_name('input')
    placeForMoney[1].send_keys('10')
    time.sleep(5)
    confirmButton = browser.find_element_by_class_name('break-word')
    # confirmButton.click()


# authorize function
def pinnacle_authorize(browser):
    browser.get('https://www.pinnacle.com/en/')
    time.sleep(10)
    username = browser.find_elements_by_id('username')

    if len(username) == 0:
        return

    password = browser.find_elements_by_id('password')
    login = browser.find_elements_by_class_name('dead-center')
    username[1].send_keys('**********')
    time.sleep(1)
    password[1].send_keys('**********')
    time.sleep(1)
    login[0].click()
    time.sleep(10)


def get_pinnacle_bets(browser):
    pinnacle_bets = []

    page = BeautifulSoup(browser.page_source, 'html.parser')
    direct_link = page.text.split('\n')[19].replace('  direct_link = \'', '').replace('\';', '')
    browser.get(direct_link)
    time.sleep(20)

    # open all blocks with bets
    block_titles = browser.find_elements_by_class_name('collapse-title')
    page_blocks = BeautifulSoup(browser.page_source, 'html.parser')
    soup_block = page_blocks.find_all('div', {'data-test-id': 'Collapse'})
    for block in range(0, len(soup_block)):
        kefs = soup_block[block].find_all('span', {'class': 'price'})
        if len(kefs) == 0:
            block_titles[block].click()

    # get bets by blocks
    page = BeautifulSoup(browser.page_source, 'html.parser')
    soup_block = page.find_all('div', {'data-test-id': 'Collapse'})
    for i in range(0, len(soup_block)):
        kefs = soup_block[i].find_all('span', {'class': 'price'})
        names = soup_block[i].find_all('span', {'class': 'label'})
        titlePre = soup_block[i].find('span', {'class': 'ellipsis'}).text
        bet_to_write = [titlePre]
        for counter in range(0, len(names)):
            if i == 0:
                bet_to_write.extend([names[counter].text.strip(),
                                     float(kefs[counter].text),
                                     counter])
            else:
                bet_to_write.extend([names[counter].text.strip(),
                                     float(kefs[counter].text),
                                     pinnacle_bets[-1][-1]+counter+1])
        pinnacle_bets.append(bet_to_write)

    return pinnacle_bets

