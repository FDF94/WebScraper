import argparse
from HTMLAnalyzer import HTMLAnalyzer
from get_html_content import get_html_content
import logging


logging.basicConfig(level=logging.DEBUG)


def ScrapeWeb(url: str, filename: str = None, excluded_blocks: list = None):

    content = get_html_content(url)

    if not content:
        return None

    parser = HTMLAnalyzer(excluded_blocks)
    parser.feed(content)

    tags = parser.get_tags_count().most_common(5)
    elements_number = parser.get_elements_count()

    if filename:
        with open(filename, "w") as f:
            f.write("There are {} HTML elements\n".format(elements_number))
            for tag, n in tags:
                f.write("Tag {} appears {} times\n".format(tag, n))
        return None
    else:
        return elements_number, tags


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", default="http://www.python.org",
                        help="URL of web page to parse.", type=str)
    parser.add_argument("-f", "--filename", default=None,
                        help="Filename in which to write results. Optional.",
                        type=str)
    parser.add_argument("--excluded_blocks", default=[], nargs="*",
                        help="""List of blocks which have
                                 content that should be disregarded""",
                        type=str)
    args = parser.parse_args()
    if args.filename is None:
        print(ScrapeWeb(args.url, excluded_blocks=args.excluded_blocks))
    else:
        ScrapeWeb(args.url, args.filename, args.excluded_blocks)
