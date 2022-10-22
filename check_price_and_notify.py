from bs4 import BeautifulSoup

import requests


url="https://market.decentraland.org/lands?assetType=nft&section=land&isMap=false&isFullscreen=false&vendor=decentraland&page=1&sortBy=cheapest&onlyOnSale=true&viewAsGuest=false&onlySmart=false"


# Make a GET request to fetch the raw HTML content

html_content = requests.get(url).text


# Parse the html content

soup = BeautifulSoup(html_content, "lxml")

print(soup.prettify()) # print the parsed data of html
