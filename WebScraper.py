import argparse
from urllib import request


def ScrapeWeb(url: str):
    with request.urlopen(url) as page:
        content = page.read().decode("utf8")

    print(content)


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", default="http://www.python.org",
                    help="URL of web page to parse", type=str)
args = parser.parse_args()
ScrapeWeb(args.url)
