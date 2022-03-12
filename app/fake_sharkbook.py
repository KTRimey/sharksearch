FEATURED_SHARKS = ['1', '3']
    
SHARKS = {
    '1': {
    'about': 'A Finnish shark.',
    'category': 'Carcharhinus macloti',
    'followed_ids': ['2','3'],
    'id': '1',
    'name': 'Heikki the Hardnose shark',
    },
    '2': {
    'about': 'A Japanese shark.',
    'category': 'Scyliorhinus tokubee',
    'followed_ids': ['5','1'],
    'id': '2',
    'name': 'Ichigo the Izu catshark',
    },
    '3': {
    'about': 'A Spanish shark.',
    'category': 'Isurus paucus',
    'followed_ids': ['4'],
    'id': '3',
    'name': 'Lucrecia the Longfin mako shark',
    },
    '4': {
    'about': 'A Vietnamese shark.',
    'category': 'Centrophorus tessellatus',
    'followed_ids': ['1'],
    'id': '4',
    'name': 'Minh the Mosaic gulper shark',
    },
    '5': {
    'about': 'An Indonesian-American shark.',
    'category': 'Negaprion brevirostris',
    'followed_ids': [],
    'id': '5',
    'name': 'Kiara the Kitefin shark',
    },
}

# fake a sharkbook
class FakeSharkbook:
    
    def get_featured_sharks(self):
        featured_sharks = []
        
        for id in FEATURED_SHARKS:
            featured_sharks.append(SHARKS[id])
            
        return featured_sharks

    def get_shark(self, id):
        return SHARKS[id]