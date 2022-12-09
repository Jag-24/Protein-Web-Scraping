from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen

products = []
prices = []
proteins =[]

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.find("h1", class_ ="css-1c6krh5 e1yn5b3f9"))
print(soup.find('title').text)
