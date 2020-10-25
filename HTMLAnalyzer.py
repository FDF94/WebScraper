from html.parser import HTMLParser
from collections import Counter


class HTMLAnalyzer(HTMLParser):

    def __init__(self):
        super().__init__()
        self._open_tags = []
        self._close_tags = []
        self._ignore_tags = False
        self._excluded_blocks = ["pre"]
        self._current_excluding = None

    def handle_starttag(self, tag, attrs):
        if not self._ignore_tags:

            self._open_tags.append(tag)

            if tag in self._excluded_blocks:
                self._current_excluding = tag
                self._ignore_tags = True

    def handle_endtag(self, tag):
        if not self._ignore_tags:
            self._close_tags.append(tag)
        # Checking self._ignore_tags again is not really necessary
        # It is left for readability
        elif self._ignore_tags and self._current_excluding == tag:
            self._ignore_tags = False
            self._current_excluding = None
            self._close_tags.append(tag)

    def get_tags_count(self):
        return Counter(self._open_tags)

    def get_elements_count(self):
        return len(self._open_tags)