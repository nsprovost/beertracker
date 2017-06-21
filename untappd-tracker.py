import requests
from bs4 import BeautifulSoup
import time
import datetime

r = requests.get('https://untappd.com/thepub')

soup = BeautifulSoup(r.content, "html.parser")

checkins = soup.find_all("div", "checkin")

for checkin in checkins:
    url = "https://untappd.com" + checkin.find_all("a", "label")[0]["href"]
    rating = checkin.select("span.rating.small")

    if rating:
        rating = int(rating[0]["class"][2][1:])
        if rating > 400:
            print str(datetime.datetime.now()) + " URL: " + url + " RATING: " + str(rating)


