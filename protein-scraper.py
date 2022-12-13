from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from Product import Product

def extract_data(url, protein):
    browser = webdriver.Firefox()
    browser.get(url)
    product_name = browser.find_element(By.TAG_NAME, 'h1').text
    product_price = browser.find_element(By.CSS_SELECTOR, 'span.css-2vqe5n.esdkp3p0').text
    return Product(product_name, product_price, protein)




p = extract_data("https://www.walmart.ca/en/ip/high-whey/6000202080561", 27)
print(p.name)
print(p.price)
print(p.protein)