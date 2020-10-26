import sys
sys.path.insert(0, '..')
import unittest
from WebScraper import ScrapeWeb
import logging
from os.path import isfile
from os import remove


logging.disable(logging.CRITICAL)


class TestWebScraper(unittest.TestCase):

    def test_file_generation(self):
        # Arrange
        url = "https://duckduckgo.com"
        filename = "TestFile.txt"

        # Act
        ScrapeWeb(url=url, filename=filename)
        file_exists = isfile(filename)

        # Assert
        self.assertTrue(file_exists, "File was not generated")
        remove(filename)


if __name__ == '__main__':
    unittest.main()
