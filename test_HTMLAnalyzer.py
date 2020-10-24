import unittest
from HTMLAnalyzer import HTMLAnalyzer
import logging
from collections import Counter


logging.disable(logging.CRITICAL)


class TestGetHtmlContent(unittest.TestCase):

    def test_elements_count(self):
        # Arrange
        parser = HTMLAnalyzer()
        sample_html = ("<html><head><title>Test</title></head>" +
                       "<body><h1>Parse me!</h1></body></html>")
        elements_result = 5

        # Act
        parser.feed(sample_html)

        # Assert
        self.assertEqual(parser.get_elements_count(), elements_result)

    def test_tags_count(self):
        # Arrange
        parser = HTMLAnalyzer()
        sample_html = ("<html><head><title>Test</title></head>" +
                       "<body><h1>Parse me!</h1></body></html>")
        tags_result = Counter(["html", "head", "title", "body", "h1"])

        # Act
        parser.feed(sample_html)

        # Assert
        self.assertEqual(parser.get_tags_count(), tags_result)


if __name__ == '__main__':
    unittest.main()
