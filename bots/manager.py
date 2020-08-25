import vprognoze
import pinnacle
import oddsfan
import time
import datetime
import csv

last_bet_id = 'news8642335'
browser = vprognoze.open_browser()
pinnacle.pinnacle_authorize(browser)
print(datetime.datetime.now())

while True:
    bets_to_place, last_bet_id = vprognoze.get_bet_info(browser, last_bet_id)
    for bet_to_place in range(0, len(bets_to_place)):
        check_fuck = oddsfan.find_match_in_oddsfan(browser, bets_to_place[bet_to_place])
        if check_fuck == -1:
            continue
        pinnacle_bets = pinnacle.get_pinnacle_bets(browser)
        pinnacle_bet_list = pinnacle.find_pinnacle_way(bets_to_place[bet_to_place], pinnacle_bets)
        pinnacle.place_bet(browser, pinnacle_bets, pinnacle_bet_list)
    print(datetime.datetime.now())
    time.sleep(180)




