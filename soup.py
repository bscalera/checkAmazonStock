#import urllib2
#from BeautifulSoup import BeautifulSoup
#import re

import requests
from bs4 import BeautifulSoup

#https://www.reddit.com/r/learnpython/comments/4eaz7v/error_503_when_trying_to_get_info_off_amazon/
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari537.36'}
#https://www.reddit.com/r/learnpython/comments/bf21fn/how_to_prevent_captcha_while_scraping_amazon/
#https://www.reddit.com/r/learnpython/comments/beomar/web_scraping_amazoncom/el7g66p?utm_source=share&utm_medium=web2x
#Contains the header information in a dictionary
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


#original page
#result = requests.get("https://www.amazon.com/HP-EliteDesk-800-G1-Refurbished/dp/B0784F3NHF", headers=headers)
result = requests.get("https://www.amazon.com/HP-EliteDesk-800-G1-Refurbished/dp/B0784F82Q5", headers=headers)

#.findNext('td')
#print(result.status_code)


#print(result.headers)

src = result.content
#print(src)
soup = BeautifulSoup(src, 'lxml')

divs = soup.find("div")
#print(links)

#for div in divs:
#  if "left in stock" in divs.text:
#    print (div)

#print(result)

#body = soup.find(text= "stock")
#print(body)





#opener = urllib2.buildopener()
#opener.addheaders = 


#search = result.find('stock')
#print ("this:", search)

#print (soup.find('stock'))

#output to file
#outF = open("output.txt", "wb")
#outF.write(soup.encode('utf-8'))
#outF.close()


textable = soup.encode('utf-8')

#for item in textable.encode().split("\n"):
#  if "stock" in item:
#    print (item.strip())


#print(textable)
#print(isinstance(textable))
#print(type(textable))

encoding = 'utf-8'
transformToString = textable.decode(encoding)
print(type(transformToString))

#for item in transformToString.encode().split("\n"):
#  if "stock" in item:
#    print (item.strip())

#with transformToString as search:
#  for line in search:
#    line.rstrip()
#    if num == line:
#      print(line)


#-------this works for In Stock
#foundStringIndex = transformToString.find("In Stock")
#print(foundStringIndex)

#shownString = transformToString[foundStringIndex : foundStringIndex+8]
#print(shownString)


foundStringIndex = transformToString.find("left in stock")
print(foundStringIndex)
if foundStringIndex > 10:
  shownString = transformToString[foundStringIndex-8 : foundStringIndex+13]
  print(shownString)

