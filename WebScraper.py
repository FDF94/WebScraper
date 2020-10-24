import argparse
from HTMLAnalyzer import HTMLAnalyzer
from get_html_content import get_html_content
import logging


logging.basicConfig(level=logging.DEBUG)


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
