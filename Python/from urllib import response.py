from urllib import response
import requests

r= requests.get()
r.text

# 1. 주소
URL = 'https://finance.naver.com/sise/'
# 2. 용청
response = requests.get(URL)
print(response)
