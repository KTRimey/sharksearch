import logging
import json
import math

from sharkbook import Sharkbook


def shark_crawl(sharkbook, max_sharks=5):
    """ crawl SharkBook data with BFS """
    
    # result to be returned
    shark_index = {}

    visited = set() # crawled sharks by id
    to_do = set() # to-do list of sharks by id

    logging.info('Starting crawl. Here sharky sharkies!')

    # add featured sharks to to-do
    for featured_shark in sharkbook.get_featured_sharks():
        to_do.add(featured_shark['id'])

    # find us some sharks (max_sharks may limit us for testing)
    while (len(to_do) > 0 and len(visited) < max_sharks):
        shark_id = to_do.pop()

        # visit shark
        shark = sharkbook.get_shark(shark_id)
    
        logging.info('Crawling... ' + shark['name'])

        # shark_index: each shark in category with name
        if shark['category'] not in shark_index:
            shark_index[shark['category']] = {}
        if shark['name'] not in shark_index[shark['category']]:
            shark_index[shark['category']][shark['name']] = []
        shark_index[shark['category']][shark['name']].append(shark)

        visited.add(shark_id)

        # connections of shark
        for friend_id in shark['followed_ids']:
            if friend_id not in visited:
                to_do.add(friend_id)

    logging.info('Finished! Total sharks crawled: {}'.format(len(visited)))

    return shark_index
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    shark_index = shark_crawl(sharkbook=Sharkbook())
    
    with open('shark_index.json', 'w') as shark_file:
        shark_file.write(json.dumps(shark_index))