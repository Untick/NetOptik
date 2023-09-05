import aiohttp
import json

class RecognizeApi:
    def __init__(self, api_url='http://api:5000'):
        self.api_url = api_url
        self.headers = {'Content-type': 'application/json'}

    async def fetch_material(self, image_url):
        data = {'url': image_url}

        async with aiohttp.request(
            method='POST', url=self.api_url + '/detect_frame_material', 
            data=json.dumps(data), 
            headers=self.headers
        ) as response:
            
            return await response.json()

    async def fetch_tag(self, _):
        return await "TAG"