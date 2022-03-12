import requests
import urllib3


class Sharkbook:
    
    def get(self, url):     
        retry = urllib3.util.retry.Retry(
           backoff_factor=0.1,
           status_forcelist=(500, 502, 503, 504),
        )
        
        adapter = requests.adapters.HTTPAdapter(max_retries=retry)
       
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