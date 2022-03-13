import unittest
from crawl import shark_crawl
from app.search import shark_search
from fake_sharkbook import FakeSharkbook, SHARKS


class TestSearch(unittest.TestCase):
    
    def test_search(self):
        
        crawl_target = FakeSharkbook()
    
        # crawl data from FakeSharkbook
        shark_index = shark_crawl(crawl_target)

        # search with query 'Heikki'
        result = shark_search('Heikki', None, shark_index)
        self.assertEqual([SHARKS['1']], result['result'])
        
        # search with query 'Izu' and category 'Scyliorhinus tokubee'
        result = shark_search('Izu', 'Scyliorhinus tokubee', shark_index)
        self.assertEqual([SHARKS['2']], result['result'])
        
        # search with query 'Minh the Milk-eye catshark'
        result = shark_search('Minh the Milk-eye catshark', None, shark_index)
        self.assertEqual([], result['result'])


if __name__ == '__main__':
  unittest.main()