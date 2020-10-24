from urllib import request
from urllib.error import URLError
import logging


logging.basicConfig(level=logging.DEBUG)


def get_html_content(url: str):
    try:
        with request.urlopen(url) as page:
            charset = page.info().get_content_charset()
            content = page.read().decode(charset)
            return content
    except ValueError:
        logging.error("Unknown URL type. This could be fixed by adding "
                      "http:// at the begin of the URL.")
        return None
    except URLError:
        logging.error("URL not found. This could be a connectivity issue.")
        return None
