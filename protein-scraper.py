from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from Product import Product
import pandas as pd
import time

start_time = time.time()

options = Options()
options.add_argument("--headless")

def extract_data(url, protein):
    browser = webdriver.Firefox(options = options)
    browser.get(url)
    product_name = browser.find_element(By.TAG_NAME, 'h1').text
    product_price = browser.find_element(By.CSS_SELECTOR, 'span.css-2vqe5n.esdkp3p0').text
    return Product(product_name, product_price, protein)


URLS = ["https://www.walmart.ca/en/ip/high-whey/6000202080561", 
"https://www.walmart.ca/en/ip/great-value-red-lentils/6000196181072",
"https://www.walmart.ca/en/ip/iso-whey/6000202081007",
"https://www.walmart.ca/en/ip/Quaker-Large-Flake-Oats/6000135892801",
"https://www.walmart.ca/en/ip/Great-Value-Natural-Crunchy-Peanut-Butter/6000198656934",
"https://www.walmart.ca/en/ip/great-value-long-grain-brown-rice/6000187054949",
"https://www.walmart.ca/en/ip/mina-halal-boneless-chicken-breasts/6000198434963",
"https://www.walmart.ca/en/ip/Great-Value-Large-Eggs/6000023483943"]

Protein = [25,9,28,4,4,3,27,6]

data = ({"Name": [], "Price": [], "Protein": []})
df = pd.DataFrame(data)

for x,y in zip(URLS,Protein):
    print("Currently working on: " + x)
    p = extract_data(x,y)
    new_row = pd.DataFrame({"Name":p.name, "Price":p.price, "Protein":p.protein}, index =[0])
    df = pd.concat([new_row,df.loc[:]]).reset_index(drop=True)

print(df)
print("---%s seconds ---" % (time.time() - start_time))