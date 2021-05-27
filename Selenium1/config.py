from selenium import webdriver
import time

driver=webdriver.Chrome(r"E:\Interview\driver\chromedriver.exe")
url=("https://downtowndallas.com/experience/stay/")
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.find_element("css selector","div > a > img").click()
time.sleep(2)
driver.find_element("link text","WHERE TO STAYCATION").click()
time.sleep(2)
driver.find_element("css selector","a.place-square__btn").click()
image = driver.find_elements_by_css_selector("body > main > div > img")[0].get_attribute("src")
print(image)
title = driver.find_element_by_css_selector("body > main > article > header > h1").text
print(title)
location = driver.find_element_by_css_selector("body > main > article > div > div.place-info > div:nth-child(1) > a ").text
print(location)
tel = driver.find_element_by_css_selector("body > main > article > div > div.place-info > div:nth-child(2) > div > a").text
print(tel)
area = driver.find_element_by_css_selector("body > main > article > div > div.place-info > div:nth-child(3) > a").text
print(area)


import requests

headers = {
    'authority': 'downtowndallas.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}

r = requests.get(image,headers=headers)
with open(f'E:/Interview/Image/{title}.png', 'wb') as f:
    f.write(r.content)
    print("Image written to files")


with open('exported.csv','a') as f:
    f.write(f"{title},{location},{tel},{area},{image}\n")