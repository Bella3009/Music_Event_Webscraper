import requests
import selectorlib

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


if __name__ == "__main__":
    scraped = scraper(url)
    print(extract(scraped))
