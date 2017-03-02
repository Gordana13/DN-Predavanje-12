from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "http://quotes.yourdictionary.com/theme/marriage/"
html = urlopen(url).read()
citati_html = BeautifulSoup(html)

citati = citati_html.findAll("p", {"class": "quoteContent"})[0:5]
for citat in citati:
        print(citat.string)
        print("-------------------------------------------------------------------------------")

