import argparse
from urllib import request
from urllib.error import URLError
from HTMLAnalyzer import HTMLAnalyzer
import logging


logging.basicConfig(level=logging.DEBUG)


def get_html_content(url: str):
    try:
        with request.urlopen(url) as page:
            return page.read().decode("utf8")
    except ValueError:
        logging.error("Unknown URL type. This could be fixed by adding "
                      "http:// at the begin of the URL.")
        return None
    except URLError:
        logging.error("URL not found.")
        return None


def ScrapeWeb(url: str):

    content = get_html_content(url)

    if content:
        parser = HTMLAnalyzer()
        parser.feed(content)

        logging.info(parser.get_tags_count())
        logging.info(parser.get_elements_count())


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", default="http://www.python.org",
                    help="URL of web page to parse", type=str)
args = parser.parse_args()
ScrapeWeb(args.url)
