import argparse
from urllib import request
from HTMLAnalyzer import HTMLAnalyzer


def ScrapeWeb(url: str):
    with request.urlopen(url) as page:
        content = page.read().decode("utf8")

    parser = HTMLAnalyzer()
    parser.feed(content)

    print(parser.get_tags_count())
    print(parser.get_elements_count())


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", default="http://www.python.org",
                    help="URL of web page to parse", type=str)
args = parser.parse_args()
ScrapeWeb(args.url)
