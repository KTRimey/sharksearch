from flask import Flask, request
from app.search import shark_search
import json


app = Flask(__name__)

@app.before_first_request
def before_first_request():
    
    shark_file = open('shark_index.json','r')

    global shark_index
    shark_index = json.loads(shark_file.read())
    
    shark_file.close()

@app.route('/search')
def search():
    # if key doesn't exist, returns a 400, bad request error
    query = request.args['query']

    # if key doesn't exist, returns None
    category = request.args.get('category')

    return shark_search(query, category, shark_index)

