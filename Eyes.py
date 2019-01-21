# libraries
import urllib2
import csv
import datetime

from bs4 import BeautifulSoup

now = datetime.datetime.now()
targets = ['https://www.bloomberg.com/feeds/bbiz/sitemap_recent.xml', 'https://trends.google.com/trends/trendingsearches/daily/rss?geo=US']
for target in targets:
    page = urllib2.urlopen(target)
    soup = BeautifulSoup(page, 'html.parser') #converts target page into soup, presumably alphabet.
    texts = soup.findAll(text=True) #creates a comma separated list elements in soup that are text
    print texts

    with open('news_headlines.csv', 'ar') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for selection in texts: #filters the urls from the CSL
            if 'articles' in selection:
                print selection
                filewriter.writerow([selection[40:50], selection[51:], now])
            elif '<b>' in selection:
                filewriter.writerow(['GGL'+str(now), selection.encode("utf-8"), now])
                print selection
                print "---------THIS IS A LINE BREAK BETWEEN SELECTIONS------------"