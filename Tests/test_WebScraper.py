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

    def test_content_generation(self):
        # Arrange
        url = "https://duckduckgo.com"

        # Act
        elements_number, tags = ScrapeWeb(url=url)

        # Assert
        with self.subTest("Positive amount of elements"):
            self.assertGreater(elements_number, 0)        
        
        with self.subTest("Tags element is not null"):
            self.assertIsNotNone(tags)


if __name__ == '__main__':
    unittest.main()
