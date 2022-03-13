import unittest
from crawl import shark_crawl
from fake_sharkbook import FakeSharkbook, SHARKS
import json
import math


class TestCrawl(unittest.TestCase):
    def test_crawl(self):
        
        crawl_target = FakeSharkbook()
    
        # crawl data from FakeSharkbook
        shark_crawl(crawl_target, max_sharks=math.inf)
        
        with open('shark_index.json','r') as shark_file: 
            shark_index = json.loads(shark_file.read())

        # assert that all fake sharks are in crawled data
        for category in shark_index:
            for name in shark_index[category]:
                self.assertTrue(shark_index[category][name][0] in SHARKS.values())
    
if __name__ == '__main__':
  unittest.main()