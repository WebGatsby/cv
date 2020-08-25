from bs4 import BeautifulSoup
import re
import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

kappers = [
"Dellas666",
"Noxxy"
]
FILENAME = 'july2020_6.csv'

# web driver call
options = Options()
options.headless = False
browser = webdriver.Firefox(options=options)
browser.get('https://vprognoze.ru/')
cookies = [{'name': 'rerf', 'value': 'AAAAAF8J3vmD0NVBAwW4Ag==', 'path': '/', 'domain': 'vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1597074425}, {'name': 'ipp_uid', 'value': '1594482425332/RgXs8PxlChvqPFvX/eHxM4v/yJsnvA1c4leNDmQ==', 'path': '/', 'domain': 'vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1924991999}, {'name': 'ipp_uid1', 'value': '1594482425332', 'path': '/', 'domain': 'vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1924991999}, {'name': 'ipp_uid2', 'value': 'RgXs8PxlChvqPFvX/eHxM4v/yJsnvA1c4leNDmQ==', 'path': '/', 'domain': 'vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1924991999}, {'name': 'login_user_token', 'value': 'a445120c8aad6cf073135070edf29298', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594525627}, {'name': '_ym_uid', 'value': '15944824331032949691', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1626018432}, {'name': '_ym_d', 'value': '1594482433', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1626018432}, {'name': '_ym_isad', 'value': '2', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594554432}, {'name': '__utmt', 'value': '1', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594483033}, {'name': 'cnt_ban_id', 'value': '1', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594486040}, {'name': 'LB_member_sc', 'value': '25e56a1a2b9ac80214fbb0ccab648057', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': True, 'expiry': 1626018440}, {'name': 'session_hash', 'value': '62491122c72804cc881c9b2dc4392420', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': True, 'expiry': 1626018440}, {'name': 'dle_user_id', 'value': '1197879', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': True, 'expiry': 1626018440}, {'name': 'dle_password', 'value': '630ea2f955d8e08bdf2c1ba81d764d0d', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': True, 'expiry': 1626018440}, {'name': 'dle_newpm', 'value': '0', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1626018440}, {'name': 'module_online', 'value': '1', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': True, 'expiry': 1594484240}, {'name': '__utma', 'value': '187128303.740933055.1594482434.1594482434.1594482434.1', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1657554441}, {'name': '__utmz', 'value': '187128303.1594482434.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1610250441}, {'name': '__utmb', 'value': '187128303.2.10.1594482434', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594484241}, {'name': '_ym_visorc_56331700', 'value': 'w', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594484241}, {'name': '_ym_visorc_5916940', 'value': 'w', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594484241}, {'name': 'autotimezone', 'value': '5', 'path': '/', 'domain': 'vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1626018444}]
for cookie in cookies:
    browser.add_cookie(cookie)
browser.refresh()

# print first row in csv
first_row = ['kapper']
for counter in range(1, 31):
    first_row.extend([str(counter)+"_profit", str(counter)+"_bets"])
with open(FILENAME, "a", newline="") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(first_row)
    file.close()

for kapper in kappers:
    bet_amount = 0
    percents_by_days = []
    days_sequence = ['0']
    percents_by_days.extend([kapper])
    for page in range(18, 0, -1):
        url = 'https://vprognoze.ru/user/' + kapper + '/news/page/' + str(page)
        try:
            browser.get(url)
        except Exception:
            time.sleep(240)
            browser.get(url)
        time.sleep(10)
        page_source = browser.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        # go by blocks
        boxes = soup.find_all('div', {'class': 'news_boxing'})
        # continue condition
        if len(boxes) == 1 or (boxes[1].find('div', {'class': 'date'}).text.find('-07-2020') == -1 and
                               boxes[len(boxes)-1].find('div', {'class': 'date'}).text.find('-07-2020') == -1):
            if len(percents_by_days) > 1:
                break
            else:
                continue

        print(page)
        for i in range(len(boxes)-1, 0, -1):
            game_date = boxes[i].find('div', {'class': 'date'}).text
            if game_date[:2].find('-') != -1:
                game_date = '0'+game_date

            if game_date.find('-07-2020') == -1:
                continue

            # Записываем количество ставок
            bet_amount = bet_amount + 1
            # Записываем процент к этому числу
            bank, perc = boxes[i].find('div', {'class': 'stats'}).text.split("(")
            # решаем, заменять или добавлять
            if str(game_date[:2]) == str(days_sequence[len(days_sequence) - 1]):
                percents_by_days[len(percents_by_days)-2] = perc.replace("%)", "")
                percents_by_days[len(percents_by_days)-1] = bet_amount
            else:
                percents_by_days.extend([perc.replace("%)", ""), bet_amount])
                days_sequence.append('0')
                days_sequence.append(game_date[:2])

    to_df = [kapper]
    for i in range(1, len(percents_by_days), 2):
        to_df.extend([percents_by_days[i], percents_by_days[i+1]])
        places_to_fill = int(days_sequence[i+1])-int(days_sequence[i-1])
        for j in range(0, places_to_fill-1):
            to_df.extend([percents_by_days[i], percents_by_days[i + 1]])

    while len(to_df) < 61:
        to_df.extend([to_df[len(to_df)-2], to_df[len(to_df)-1]])

    # write in csv file
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(to_df)
        file.close()
        print(kapper)
        print('-------------------------------------------------------------------------------------------------------')
