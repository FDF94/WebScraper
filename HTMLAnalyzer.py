from html.parser import HTMLParser
from collections import Counter
import logging


class HTMLAnalyzer(HTMLParser):

    def __init__(self, excluded_blocks=None):
        super().__init__()
        self._open_tags = []
        self._close_tags = []
        self._ignore_tags = False
        self._current_excluding = None
        if excluded_blocks:
            self._excluded_blocks = excluded_blocks
        else:
            self._excluded_blocks = []

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
        open_counter = Counter(self._open_tags)
        close_counter = Counter(self._close_tags)
        if open_counter != close_counter:
            logging.warning("Opening and closing tag numbers do not match")
        return open_counter

    def get_elements_count(self):
        opening_elements = len(self._open_tags)
        closing_elements = len(self._close_tags)
        if opening_elements != closing_elements:
            logging.warning("Opening and closing elements"
                            " numbers do not match")
        return opening_elements
