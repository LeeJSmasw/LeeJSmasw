import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By




#파이썬 터미널과 쥬피터 노트북 터미널 차이가 무엇일까

# pip install pandas
# pip install selenium
# pip install lxml

browser = webdriver.Chrome()
browser.maximize_window()

#chrome drive
#chrome://version/

url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page=2'
#url 구조를 따는것부터가 흥미로운데.. 
browser.get(url)


#selnium 시가 홈페이지 접소 홈페이지 