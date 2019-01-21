# libraries
import urllib2
import csv
import datetime

from bs4 import BeautifulSoup

now = datetime.datetime.now()
targets = ['https://www.bloomberg.com/feeds/bbiz/sitemap_recent.xml', 'https://trends.google.com/trends/trendingsearches/daily/rss?geo=US', 'https://trends.google.com/trends/trendingsearches/daily/rss?geo=GB', 'https://www.cnbc.com/id/100003114/device/rss/rss.html', 'https://www.cnbc.com/id/100727362/device/rss/rss.html', 'https://www.cnbc.com/id/15837362/device/rss/rss.html', 'https://www.cnbc.com/id/19832390/device/rss/rss.html', 'https://www.cnbc.com/id/10001147/device/rss/rss.html', 'https://www.cnbc.com/id/10000664/device/rss/rss.html', 'https://www.cnbc.com/id/19854910/device/rss/rss.html', 'https://www.cnbc.com/id/10000113/device/rss/rss.html']
for target in targets:
    page = urllib2.urlopen(target)
    soup = BeautifulSoup(page, 'html.parser') #converts target page into soup, presumably alphabet.
    texts = soup.findAll(text=True) #creates a comma separated list of the elements in soup that are text
    print texts

    with open('news_headlines.csv', 'ar') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for selection in texts: #filters the urls from the CSL
            if 'bloomberg' in selection: #bloomberg
                print selection
                filewriter.writerow([now, selection[51:], 'BBG']) #published date, headline, recording date
            elif '<b>' in selection: #google trending headline
                filewriter.writerow([now, selection.encode("utf-8"), 'GGL']) #effective "publishing" date with GGL prefix, headline, recording date
                print selection
                print "---THIS IS A LINE BREAK---"
            elif 'cnbc' in target:
                if len(selection) > 20:
                    if 'GMT' in selection:
                        continue
                    filewriter.writerow([now,selection.encode("utf-8"), 'CNBC'])
                    print selection
                    print "---THIS IS A LINE BREAK---"


