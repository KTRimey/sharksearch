import unittest

from crawl import shark_crawl
from fake_sharkbook import FakeSharkbook, SHARKS


class TestCrawl(unittest.TestCase):
    
    def test_crawl(self):
        
        # crawl data from FakeSharkbook
        shark_index = shark_crawl(sharkbook=FakeSharkbook())
        
        # assert that all crawled sharks are in fake data
        for category in shark_index:
            for name in shark_index[category]:
                for shark in shark_index[category][name]:
                    self.assertTrue(shark in SHARKS.values())
                
        # assert that all fake sharks are in crawled data 
        for fake_shark in SHARKS.values():
            category = fake_shark['category']
            name = fake_shark['name']
            self.assertTrue(fake_shark in shark_index[category][name])
    
if __name__ == '__main__':
  unittest.main()