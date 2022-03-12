# search for sharks!
def shark_search(query, category, shark_index):
    matched = []

    # category was passed as a parameter
    if (category != None): 
         # exact match category
        if category in shark_index:
            # substring match query
            for name in shark_index[category]: 
                if query in name:
                    shark = shark_index[category][name]
                    matched.extend(shark)
    # substring match query
    else:
        for category in shark_index:
            for name in shark_index[category]:
                if query in name:
                    shark = shark_index[category][name]
                    matched.extend(shark)

    return {'result': matched}