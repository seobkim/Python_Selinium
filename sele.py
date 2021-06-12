import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import os

r = open('C:\\Users\\negga\\Desktop\\pypy\\martquery.txt', mode='rt', encoding='utf-8')
txtlist = []

print('------------------------------------------')
for line in r:
    line=line.replace('\n','')
    print(line)
    txtlist += [line]
r.close()
print('------------------------------------------')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options

import time
import sys, os, time
import datetime
from requests import get 
ip = ""
while(True):
        if(ip!=get("https://api.ipify.org").text):
            print('변경 전 IP : ' , ip)
            ip = get("https://api.ipify.org").text
            print('변경 후 IP : ' , ip)

            for i in txtlist:    
                
                now= datetime.datetime.now()
                nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
                
                print(nowDatetime)
                print('검색조건 : ',i)

                if  getattr(sys, 'frozen', False): 
                    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
                    driver = webdriver.Chrome(chromedriver_path)
                
                
                driver.get(url='https://www.naver.com/')

                try:
                    search_box = driver.find_element_by_id('query')
                    time.sleep(3)
                    search_box.send_keys(i)
                    time.sleep(3)
                    search_btn = driver.find_element_by_id('search_btn')
                    time.sleep(3)
                    search_btn.click()
                
                    shop_more_btn = driver.find_element_by_css_selector('a.api_more._link')
                    shop_more_btn.click()
                
                
                    ###############새로운 윈도우창 컨트롤################
                    for handle in driver.window_handles:
                        print(handle)
                    driver.switch_to_window(driver.window_handles[1])
                    #####################################################
                
                
                
                    ###############스크롤을 내려 동적데이터들 load#######
                    time.sleep(5)
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    time.sleep(5)
                    #####################################################
                
                
                
                    ###############현재 페이지의 상좀목록 가져옴##############
                    find_shop_name = driver.find_elements_by_css_selector('.basicList_mall__sbVax')
                    ##########################################################
                
                
                
                    ###################페이지 이동버튼#######################
                    paging_btn = driver.find_elements_by_css_selector('.pagination_btn_page__FuJaU')
                    select_page_btn = driver.find_element_by_css_selector('.pagination_btn_page__FuJaU.active')
                    #########################################################
                
                    find_flag = 1 #찾으면 반복문 끝낼거
                    for i in range(len(paging_btn)):
                        if(find_flag):
                            ###############현재 페이지의 상좀목록 가져옴##############
                            find_shop_name = driver.find_elements_by_css_selector('.basicList_mall__sbVax')
                            ##########################################################
                            for j in find_shop_name:
                                if(j.text == '민수마트'):
                                    j.find_element_by_xpath('../../.././div[1]/div[1]/a[1]').click()
                                    find_flag = 0
                                    print(j.text,'ok')
                            
                            if(find_flag):
                                paging_btn[i+1].click()
                                time.sleep(5)
                                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                        else:
                            break
                
                except:
                    print('예외가 발생했습니다.')
                    continue
                finally:
                    time.sleep(5)
                    driver.quit()

