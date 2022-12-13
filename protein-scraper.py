from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

#Arrays for storing products, prices and protein content 
products = []
prices = []
proteins =[]

#BeautifulSoup html extraction method
url = "https://www.walmart.ca/en/ip/high-whey/6000202080561"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"}
html = requests.get(url, headers = headers)

#Selenium html and JS extraction method
browser = webdriver.Firefox()
browser.get("https://www.walmart.ca/en/ip/high-whey/6000202080561")

#Method of extraction of data using both BeautifulSoup and Selenium
soup_test = BeautifulSoup(browser.page_source, 'html.parser')
soup = BeautifulSoup(html.text, features='html.parser')
product_name = soup.find('h1', attrs={'data-automation':'product-title'}).text
product_price = browser.find_element(By.CSS_SELECTOR, 'span.css-2vqe5n.esdkp3p0').text

#test prints to verfiy data extraction
print(product_name)
print(product_price)