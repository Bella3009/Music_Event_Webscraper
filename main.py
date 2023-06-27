import requests
import selectorlib
from sendEmail import send_email
import time

url = "http://programmer100.pythonanywhere.com/tours/"
Headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; '
                         'Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 Safari/537.36'}


def scraper(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=Headers)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def store(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read():
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    while True:
        scraped = scraper(url)
        extracted = extract(scraped)
        print(extracted)
        content = read()
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email("New event was found")
        time.sleep(2)
