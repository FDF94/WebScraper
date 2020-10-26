import sys
sys.path.insert(0, '..')
import unittest
from get_html_content import get_html_content
import logging


logging.disable(logging.CRITICAL)


class TestGetHtmlContent(unittest.TestCase):

    def test_get_content(self):
        # Arrange
        url = "https://www.endava.com/"

        # Act
        content = get_html_content(url)

        # Assert
        self.assertIsNotNone(content)

    def test_get_content_fail_scenarios(self):
        with self.subTest("Invalid URL type"):
            # Arrange
            url = "www.endava.com/"

            # Act
            content = get_html_content(url)

            # Assert
            self.assertIsNone(content)
        with self.subTest("Unexistant URL"):
            # Arrange
            # As I'm writing this, it doesn't exist
            url = "http://www.CompletelyFakeURL.com/"

            # Act
            content = get_html_content(url)

            # Assert
            self.assertIsNone(content)


if __name__ == '__main__':
    unittest.main()
