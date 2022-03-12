from app import app

# crawl SharkBook data with BFS
def shark_crawl(sharkbook, max_sharks):
    
    # data structure
    shark_index = {}

    visited = set() # crawled sharks by id
    to_do = set() # to-do list of sharks by id

    app.logger.info('Starting crawl. Here sharky sharkies!')

    # start from a featured shark
    for featured_shark in sharkbook.get_featured_sharks():
        to_do.add(featured_shark['id'])

    # find us some sharks (max_sharks may limit us for testing)
    while (len(to_do) > 0 and len(visited) < max_sharks):
        shark_id = to_do.pop()

        # visit shark
        shark = sharkbook.get_shark(shark_id)
    
        app.logger.info('Crawling... ' + shark['name'])

        # shark_index: each shark in category with name
        if shark['category'] in shark_index:
            if shark['name'] in  shark_index[shark['category']]:
                shark_index[shark['category']][shark['name']].append(shark)
            else:
                shark_index[shark['category']][shark['name']] = [shark]
        else:
            shark_index[shark['category']] = {shark['name']: [shark]}

        # connections of shark
        for friend_id in shark['followed_ids']:
            if friend_id not in visited:
                to_do.add(friend_id)

        visited.add(shark_id)

    app.logger.info('Finished! Total sharks crawled: {}'.format(len(visited)))

    return shark_index