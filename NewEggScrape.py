from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48'

uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
# we parse the page as html

containers = page_soup.findAll("div", {"class" : "item-container"})
# we take all graphic cards

filename = 'products.csv'
f = open(filename, "w", newline='')

headers = "Brand" + "," +  "Product" + "," + "Price" + "," + "Shipping" + "\n"
f.write(headers)

# Another way of doing this could be as follows:
# writer = csv.writer(f, delimiter=',')
# writer.writerow(['Brand', 'Product', 'Price', 'Shipping'])

for container in containers: 
    containerBrand = container.find("a", {"class": "item-brand"})
    containerBrandName = containerBrand.img["title"]

    containerProduct = container.find("a", {"class": "item-title"})
    containerProductName = containerProduct.get_text()

    containerPrice = container.find("li", {"class" : "price-current"})
    containerPriceCurrent = containerPrice.find("strong")
    containerProductPrice = containerPriceCurrent.get_text()

    containerPriceShipping = container.find("li", {"class":"price-ship"})
    containerPriceShip = containerPriceShipping.get_text().strip()

    print("Brand: " + containerBrandName)
    print("Product: " + containerProductName)
    print("Price: " + containerProductPrice)
    print("Shipping Price: "  + containerPriceShip)

    f.write(containerBrandName + "," + containerProductName.replace(",", "||") + "," + containerProductPrice + "," + containerPriceShip + "\n")
    # we replace the colon in the  product Name so it doesn't take it as another item to wite

    # writer.writerow([containerBrandName, containerProductName.replace(",", "||"), containerProductPrice.replace(",", "."), containerPriceShip])
    
f.close()
