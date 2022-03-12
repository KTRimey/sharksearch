from flask import Flask, request
import math

app = Flask(__name__)

# import after after defining app to avoid a circular dependecy
from app.crawl import shark_crawl
from app.search import shark_search
from app.sharkbook import Sharkbook

@app.route('/search')
def search():
    # if key doesn't exist, returns a 400, bad request error
    query = request.args['query']

    # if key doesn't exist, returns None
    category = request.args.get('category')

    return shark_search(query, category, shark_index)

# sharkbook to crawl
crawl_target = Sharkbook()

# limit on number of sharks to crawl (no limit: math.inf)
crawl_limit = 10
 
# crawl data on startup 
shark_index = shark_crawl(crawl_target, crawl_limit)