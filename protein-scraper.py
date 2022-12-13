from bs4 import BeautifulSoup
import requests
import requests

products = []
prices = []
proteins =[]

url = "https://www.walmart.ca/en/ip/high-whey/6000202080561"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"}
html = requests.get(url, headers = headers)

soup = BeautifulSoup(html.text, features='html.parser')
product_name = soup.find('h1', attrs={'data-automation':'product-title'}).text
product_price = soup.find('span', attrs={'data-automation':'buybox-price'})
#Test_Desc = soup.find('h1', attrs={'data-automation':'product-title'}).text

print(product_name)
#print(product_price)
#print(Test_Desc)