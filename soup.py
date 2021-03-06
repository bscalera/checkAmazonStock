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

#you can get the status code for the page
#print(result.status_code)

#print(result.headers)


src = result.content

#lxml needs to be installed separately
soup = BeautifulSoup(src, 'lxml')

#Change from soup object to byte object
textable = soup.encode('utf-8')

#Change from byte object to string object
encoding = 'utf-8'
transformToString = textable.decode(encoding)
#Print object type
print(type(transformToString))



#-------this works for In Stock
#foundStringIndex = transformToString.find("In Stock")
#print(foundStringIndex)
#shownString = transformToString[foundStringIndex : foundStringIndex+8]
#print(shownString)

#This works for only a few left in stock
#Find the place on the page where it says the number left in stock
foundStringIndex = transformToString.find("left in stock")
#print the index where left in stock was found
print(foundStringIndex)
#If it was found, show the number left in stock
if foundStringIndex > 10:
  shownString = transformToString[foundStringIndex-8 : foundStringIndex+13]
  print(shownString)

