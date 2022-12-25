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

def user(descision):
    if descision == "Y":
        return True
    elif descision == "N":
        return False
    else: 
        return "Unexpected input"

def Data_creation(URLS, Protein):
    data = ({"Name": [], "Price": [], "Protein": []})
    df = pd.DataFrame(data)
    for x,y in zip(URLS,Protein):
        print("Currently working on: " + x)
        p = extract_data(x,y)
        new_row = pd.DataFrame({"Name":p.name, "Price":p.price, "Protein":p.protein}, index =[0])
        df = pd.concat([new_row,df.loc[:]]).reset_index(drop=True)
    return df


URLS = ["https://www.walmart.ca/en/ip/high-whey/6000202080561", 
"https://www.walmart.ca/en/ip/great-value-red-lentils/6000196181072",
"https://www.walmart.ca/en/ip/iso-whey/6000202081007",
"https://www.walmart.ca/en/ip/Quaker-Large-Flake-Oats/6000135892801",
"https://www.walmart.ca/en/ip/Great-Value-Natural-Crunchy-Peanut-Butter/6000198656934",
"https://www.walmart.ca/en/ip/great-value-long-grain-brown-rice/6000187054949",
"https://www.walmart.ca/en/ip/mina-halal-boneless-chicken-breasts/6000198434963",
"https://www.walmart.ca/en/ip/Great-Value-Large-Eggs/6000023483943"]

New_URLS =[]

Protein = [25,9,28,4,4,3,27,6]

New_Protein= []

user_statement = input("Would you like to use a pre-determined list of URL's (Y/N)?")

if user(user_statement) == False:
    add_or_no = input("Would you like to add to the default list(A) or create a new one(B) (A/B)?")
    if add_or_no == "A":
        x = 0
        adding = int(input("How many URL's would you like to add (integer)?"))
        while x < adding:
            url = input("Please enter a URL:")
            pro = int(input("Please enter the associated protein per serving (integer):"))
            Protein.append(pro)
            URLS.append(url)
            x += 1
        print("Executing...")
        print(Data_creation(URLS, Protein))
    elif add_or_no == "B":
        x = 0
        adding = int(input("How many URL's would you like to add (integer)?"))
        while x < adding:
            url = input("Please enter a URL:")
            pro = int(input("Please enter the associated protein per serving (integer):"))
            New_Protein.append(pro)
            New_URLS.append(url)
            x += 1
        print("Executing...")
        print(Data_creation(New_URLS, New_Protein))
    else:
        print("Unrecognized input please try again later...")

elif user(user_statement) == True:
    print("Executing...")
    print(Data_creation(URLS, Protein))

else:
    print("Unrecogized input please try again later...")


#for x,y in zip(URLS,Protein):
#    print("Currently working on: " + x)
#    p = extract_data(x,y)
#    new_row = pd.DataFrame({"Name":p.name, "Price":p.price, "Protein":p.protein}, index =[0])
#    df = pd.concat([new_row,df.loc[:]]).reset_index(drop=True)

#print(Data_creation)
#print("---%s seconds ---" % (time.time() - start_time))