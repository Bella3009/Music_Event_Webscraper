import requests
import selectorlib
from sendEmail import send_email
import time
import sqlite3

url = "http://programmer100.pythonanywhere.com/tours/"
Headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; '
                         'Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("data.db")


class Event:
    def scraper(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=Headers)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Events VALUES(?,?,?)", row)
    connection.commit()


def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Events WHERE Band=? AND City=? AND Date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows


if __name__ == "__main__":
    while True:
        event = Event()
        scraped = event.scraper(url)
        extracted = event.extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            content = read(extracted)
            # Check the list is not empty
            if not content:
                store(extracted)
                send_email("New event was found")
                print("Email sent")
        time.sleep(2)
