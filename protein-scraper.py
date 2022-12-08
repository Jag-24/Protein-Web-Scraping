from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Safari()

products = []
prices = []
proteins =[]
driver.get("https://www.walmart.ca/en/ip/high-whey/6000202080561")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class':'js-content'}):
    price = a.find('div', attrs={'class':'css-2vqe5n esdkp3p0'})
    name = a.find('div', attrs={'class':'css-jl2ki2 e1yn5b3f3'})
    #amount = a.find('div', attrs={'class':''})

    products.append(name.text)
    prices.append(price.text)

df = pd.DataFrame({'Name':products,'Price':prices})
df.to_csv('products.csv', index=False, encoding='utf-8')