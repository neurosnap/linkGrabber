""" Unit test ScrapeLinks functionality"""
import os.path
import unittest
import bs4

from linkGrabber import Links


class TestScrape(unittest.TestCase):
    """ A set of unit tests for ScrapeLinks """
    def setUp(self):
        """ Activated on start up of class """
        self.url = "http://www.google.com"
        self.bad_url = "www.google.com"
        # grab some example html pages to test
        base_dir = os.path.dirname(os.path.realpath(__file__))
        pages = ["google.html", "freep.html"]
        self.page_texts = []
        for page in pages:
            with open(os.path.join(base_dir, 'pages', page)) as fp:
                self.page_texts.append(fp.readlines())

    def test_url(self):
        """ Validate URL on instance instantiation """
        self.assertRaises(Exception, Links, self.bad_url)

    def test_soup_property(self):
        """ Getting the web page yields correct response"""
        seek = Links(self.url)
        self.assertIsInstance(seek._soup, bs4.BeautifulSoup)

    def test_find_bad_filter_param(self):
        """ Bad filter param inputs """
        seek = Links(self.url)
        self.assertRaises(Exception, seek.find, filters=25)
        self.assertRaises(Exception, seek.find, filters=['href', 'style'])

    def test_find_limit_param(self):
        """ How does find() handle the limit property """
        seek = Links(self.url)
        self.assertEqual(len(seek.find(limit=5)), 5)
        self.assertEqual(len(seek.find(limit=1)), 1)

    def test_find_number_of_links(self):
        """ Ensure expected number of links 
        reflects actual number of links """

    def test_find_reverse_sort(self):
        """ Ensure reverse sort does what it 
        is told"""

    def test_find_seo(self):
        """ Ensure SEO is properly parsed """

    def test_find_sort_by_text(self):
        """ Sorting by text name produces
        proper results """

    def test_find_sort_by_href(self):
        """ Sorting by href produces
        proper results """

if __name__ == '__main__':
    unittest.main(verbosity=2)
