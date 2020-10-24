from urllib import request
from urllib.error import URLError
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
        logging.error("URL not found. This could be a connectivity issue.")
        return None
