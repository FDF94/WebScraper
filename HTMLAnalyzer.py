from html.parser import HTMLParser
from collections import Counter


class HTMLAnalyzer(HTMLParser):

    def __init__(self):
        super().__init__()
        self._open_tags = []

    def handle_starttag(self, tag, attrs):
        self._open_tags.append(tag)

    def handle_endtag(self, tag):
        pass

    def get_tags_count(self):
        return Counter(self._open_tags)

    def get_elements_count(self):
        return len(self._open_tags)
