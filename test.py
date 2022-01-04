# -*- coding: utf-8 -*-

import os
import sys
import datetime as dt
from time import sleep
from random import randint
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def open_browser():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome("chromedriver", chrome_options=options)
    return driver

def run():
    driver = open_browser()
    driver.get('https://etk.srail.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000') #로그인페이지
    driver.implicitly_wait(3)
    driver.find_element_by_id('srchDvNm01').send_keys("1993074760") #아이디
    driver.find_element_by_id('hmpgPwdCphd01').send_keys("198959park") #비번
    driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click() #로그인 클릭
    #sleep(0.4)
    driver.implicitly_wait(3)
    print(driver.window_handles)
    driver_count = len(driver.window_handles)
    print(driver_count)
    if driver_count != 1:  #팝업창 없애는 부분
        driver_count = driver_count - 1
        driver.switch_to.window(driver.window_handles[driver_count]) 
        driver.close()
    
    driver.implicitly_wait(3)
    driver.switch_to.window(driver.window_handles[0])#메인창으로 포커스 옮김
    driver.implicitly_wait(3)

    
    
    driver.find_element_by_xpath('//*[@id="dptRsStnCd"]/option[text()=''"{}"]'.format(dpt)).click()#출발지
    driver.find_element_by_xpath('//*[@id="arvRsStnCd"]/option[text()=''"{}"]'.format(arv)).click()#도착지

    #인원수
    #시간

    driver.implicitly_wait(10)

    driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/div[3]/div/input[1]').click() #원하는 시간대 찾기, 달력클릭
    driver.implicitly_wait(10)


    driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/a').click() # 객실찾기버튼

    
    
    
    #원하는 시간 입력

    
    sleep(30)


if __name__ == "__main__":
    dpt = input("출발지 입력 (ex 동탄, 울산, 동대구, 수서, 천안아산) : ")
    arv = input("도착지 입력 - 출발지랑 마찬가지 \n")
    #ppls = input("인원수 입력")
    while True:
        dpt_month = int(input("월(month) 입력 : "))
        print(dt.datetime.now().month)
        if dpt_month < dt.datetime.now().month or dpt_month > dt.datetime.now().month+1:
            print("예매는 1개월 안에만 가능합니다.")
        else:
            break

    dpt_date = input("일(date) 입력 : ")
    #print(dpt_date)
    #when = input("열차시간 : ")

    run()