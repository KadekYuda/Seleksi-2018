import time
import json
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# example for small singular URL
example_url = "https://www.mobil123.com/dijual/honda-jazz-rs-jawa-barat-bekasi-barat/4780232"

# example for a collection of 10 url (a page)
example2_url = "https://www.mobil123.com/mobil-dijual/indonesia?type=used&page_number=1&page_size=10"

def URLCrawler(url):
	print("    Scrapping " + url)
	# open connection and grabbing the webpage
	page_html = getHTML(url)

	# parse html
	page_soup = soup(page_html, "html.parser")

	# take the data needed
	specs = page_soup.find("div", {"class":"listing__key-listing__list"}).findAll("div",{"class":"list-item"})
	seller_details = page_soup.findAll("div",{"class":"listing__seller__list__item"})
	location = seller_details[1].text.strip().split(" » ")

	price = ""
	make = ""
	model = ""
	variant = ""
	year = ""
	engine_cap = ""
	transmission = ""
	passenger_cap = ""
	mileage = ""
	color = ""
	seller = ""

	for spec in specs:
		content = spec.span.text
		if (content == "Merek"):
			make = spec.find("span",{"itemprop":"manufacturer"}).text
		elif (content == "Model"):
			model = spec.find("span",{"itemprop":"model"}).text
		elif (content == "Varian"):
			variant = spec.find("span",{"class":"float--right"}).text
		elif (content == "Tahun"):
			year = spec.find("span",{"class":"float--right"}).text
		elif (content == "Cakupan mesin"):
			engine_cap = spec.find("span",{"class":"float--right"}).text
		elif (content == "Transmisi"):
			transmission = spec.find("span",{"class":"float--right"}).text
		elif (content == "Penumpang"):
			passenger_cap = spec.find("span",{"class":"float--right"}).text
		elif (content == "Kilometer"):
			mileage = spec.find("span",{"class":"float--right"}).text + " km"
		elif (content == "Warna"):
			color = spec.find("span",{"class":"float--right"}).text
		price = page_soup.find("meta", {"name":"ga:cad:details:price"})["content"]
		seller = seller_details[0].text.strip()
		loc_province = location[0]
		loc_city = location[1]

	# return json-like dict
	result ={	
		"price"         : price,
		"make"          : make,
		"model"         : model,
		"variant"       : variant,
		"year"          : year,
		"engine_cap"    : engine_cap,
		"transmission"  : transmission,
		"passenger_cap" : passenger_cap,
		"mileage"		: mileage,
		"color"         : color,
		"seller"		: seller,
		"loc_province"  : loc_province,
		"loc_city"      : loc_city
	}
	return result

def PageCrawler(url):
	# get html page
	page_html = getHTML(url)
	
	# parse html page
	page_soup = soup(page_html, "html.parser")

	# getting all the links for a page
	container = page_soup.findAll("article",{"class":"listing"})
	data = []
	for elements in container:
		result = URLCrawler(elements.a["href"])
		data.append(result)
		time.sleep(10)
	return data

def WebCrawler(pages, link_per_page):
	# the designated url to be crawled
	data = []
	for pg_num in range(pages):
		url = "https://www.mobil123.com/mobil-dijual/indonesia?type=used&page_number="+str(pg_num+1)+"&page_size="+str(link_per_page)
		print("Scrapping from " + url)
		result = PageCrawler(url)
		data = data + result
		time.sleep(5)
	return data


def getHTML(url):
	# open connection and grabbing the webpage
	# use Mozilla and Chrome user agent to prevent ban
	uClient = urlopen(url)
	page_html = uClient.read()
	uClient.close()
	return page_html

def writeJSON(path, fileName, data):
	filePathName = './' + path + '/' + fileName + '.json'
	with open(filePathName, 'w') as fp:
		json.dump(data, fp, indent = 2, separators=(',',':'))


# the script starts from here
result = WebCrawler(10, 50)
# define time at the time scrapping is finished
now = datetime.datetime.now()
# use the time to name result file
fileName = str(now.year) + str(now.month) + str(now.day) + "-" + str(now.hour) + str(now.minute) + str(now.second)
# I put the result file  in the ../data folder
path = '../data'
writeJSON(path, fileName, result)
# show success message
print("\nTotal data crawled: " + str(len(result)))
print("Successfully written result to ../data/"+fileName+".json!!")