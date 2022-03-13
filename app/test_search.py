import unittest

from crawl import shark_crawl
from app.search import shark_search
from fake_sharkbook import FakeSharkbook, SHARKS


class TestSearch(unittest.TestCase):
    
    def test_search(self):
        
        # crawl data from FakeSharkbook
        shark_index = shark_crawl(sharkbook=FakeSharkbook())

        # search with query 'Heikki'
        result = shark_search('Alicia', None, shark_index)
        self.assertEqual(result['result'], [SHARKS['1']])
        
        # search with query 'Izu' and category 'Scyliorhinus tokubee'
        result = shark_search('Izu', 'Scyliorhinus tokubee', shark_index)
        self.assertEqual(result['result'], [SHARKS['2']])
        
        # search with query 'Minh the Milk-eye catshark'
        result = shark_search('Minh the Milk-eye catshark', None, shark_index)
        self.assertEqual(result['result'], [])


if __name__ == '__main__':
  unittest.main()