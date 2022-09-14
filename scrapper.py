import requests
from bs4 import BeautifulSoup
req = requests.get("enterwebsiteURLhere")

soup=BeautifulSoup(req.content, "html.parser")

print(soup.prettify())
