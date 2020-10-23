import argparse
from urllib import request
from urllib.error import URLError
from HTMLAnalyzer import HTMLAnalyzer


def ScrapeWeb(url: str):
    try:
        with request.urlopen(url) as page:
            content = page.read().decode("utf8")
    except ValueError:
        print("Unknown URL type. This could be fixed by adding "
              "http:// at the begin of the URL.")
        return -1
    except URLError:
        print("URL not found.")
        return -1

    parser = HTMLAnalyzer()
    parser.feed(content)

    print(parser.get_tags_count())
    print(parser.get_elements_count())


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", default="http://www.python.org",
                    help="URL of web page to parse", type=str)
args = parser.parse_args()
ScrapeWeb(args.url)
