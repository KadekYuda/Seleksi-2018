from urllib.request import urlopen as urlReq
from bs4 import BeautifulSoup as soup

# example for small singular URL
example_url = "https://www.mobil123.com/dijual/honda-jazz-rs-jawa-barat-bekasi-barat/4780232"

def childURLCrawler(url):
	print("Scrapping " + url)
	# open connection and grabbing the webpage
	uClient = urlReq(url)
	page_html = uClient.read()
	uClient.close()

	# parse html
	page_soup = soup(page_html, "html.parser")

	# take the data needed
	specs = page_soup.find("div", {"class":"listing__key-listing__list"}).findAll("div",{"class":"list-item"})
	seller_details = page_soup.findAll("div",{"class":"listing__seller__list__item"})
	location = seller_details[1].text.strip().split(" » ")

	price = page_soup.find("meta", {"name":"ga:cad:details:price"})["content"]
	make = specs[1].find("span",{"itemprop":"manufacturer"}).text
	model = specs[2].find("span",{"itemprop":"model"}).text
	variant = specs[3].find("span",{"class":"float--right"}).text
	year = specs[4].find("span",{"class":"float--right"}).text
	engine_cap = specs[5].find("span",{"class":"float--right"}).text
	transmission = specs[6].find("span",{"class":"float--right"}).text
	passenger_cap = specs[7].find("span",{"class":"float--right"}).text
	milage = specs[8].find("span",{"class":"float--right"}).text
	color = specs[9].find("span",{"class":"float--right"}).text
	seller = seller_details[0].text.strip()
	loc_province = location[0]
	loc_city = location[1]

	# for testing purposes
	print("price : " + price)
	print("make : " + make)
	print("model : " + model)
	print("variant : " + variant)
	print("year : " + year)
	print("engine_cap : " + engine_cap)
	print("transmission : " + transmission)
	print("passenger_cap : " + passenger_cap)
	print("milage : " + milage)
	print("color : " + color)
	print("seller : " + seller)
	print("loc_province : " + loc_province)
	print("loc_city : " + loc_city)

	# insert into json (?)

childURLCrawler(example_url)