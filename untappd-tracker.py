import requests
from bs4 import BeautifulSoup
import datetime
import boto3
import tempfile


def parse_the_pub_html():
    r = requests.get('https://untappd.com/thepub')

    soup = BeautifulSoup(r.content, "html.parser")

    checkins = soup.find_all("div", "checkin")

    output = tempfile.TemporaryFile()
    for checkin in checkins:
        url = "https://untappd.com" + checkin.find_all("a", "label")[0]["href"]
        rating = checkin.select("span.rating.small")

        if rating:
            rating = int(rating[0]["class"][2][1:])
            output.write(
                str(datetime.datetime.now()) + " URL: " + url + "RATING: " +
                str(rating) + "\n"
            )

    output.seek(0)
    return output

def untappd_data_scraper_handler():
    s3_client = boto3.client('s3')
    output = parse_the_pub_html()
    # Upload the file to S3
    s3_client.upload_fileobj(output, 'craftmaster', 'output/test.txt')

if __name__ == "__main__":
    untappd_data_scraper_handler()
