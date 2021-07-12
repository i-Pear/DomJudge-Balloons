import os
from selenium import webdriver
import datetime
import time
from selenium.webdriver.support.ui import WebDriverWait
from os import path
from selenium.webdriver import DesiredCapabilities

driver = webdriver.Chrome()

dealt = {}
stack = []
delay = 2

driver.get('192.168.19.250')
input('Log in and TURN OFF AUTO REFRESH')

while True:
    time.sleep(delay)
    delay = 2
    print('!!! Start Syncing data >>>')
    driver.refresh()
    WebDriverWait(driver,10).until(lambda x: len(x.find_elements_by_xpath('/html/body/div/div/div/div[2]/table')))
    table = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/table')
    # 封榜前为div[2] 封榜后为div[3]
    lines = table.find_elements_by_tag_name('tr')
    reduplication = 0
    for line in lines:
        tds = line.find_elements_by_tag_name('td')
        runID = int(tds[1].text)
        if runID in dealt:
            reduplication += 1
            if reduplication > 5:
                break
            continue
        delay = 0
        submitTime = tds[2].text
        color = tds[3].text
        team = tds[4].text
        dealt[runID] = 1
        stack.append((runID, color, submitTime, team))
        print('>>> Inserted: runID=' + str(runID) + '  SubmitTime=' + submitTime + '  TeamName=' + team)
    print('>>> Sync Finished !!!\n\n')
    while len(stack) > 0:
        input('! Publish: Color=' + str(stack[-1][1]) + '-' + str(stack[-1][3][2:5]) + '  runID=' + str(stack[-1][0])
              + '  TeamName=' + str(stack[-1][3]) + '  Time=' + str(stack[-1][2]) + '\n\n')
        stack.pop()
