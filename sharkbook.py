import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# the real sharkbook
class Sharkbook:
    
    def get(self, url):     
        retry = Retry(
           backoff_factor=0.1,
           status_forcelist=(500, 502, 503, 504),
        )
        
        adapter = HTTPAdapter(max_retries=retry)
       
        session = requests.Session()
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        response = session.get(url, headers={'accept': 'application/json'})
        response.raise_for_status()
        
        return response.json()

    def get_featured_sharks(self):
        sharks = self.get('https://sharkbook.matchmade.tv')
        return sharks['featured_users']

    def get_shark(self, id):
        return self.get('https://sharkbook.matchmade.tv/users/' + str(id))