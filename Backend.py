import requests
import selectorlib

url = "http://programmer100.pythonanywhere.com/tours/"


def scraper(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


if __name__ == "__main__":
    print(scraper(url))
