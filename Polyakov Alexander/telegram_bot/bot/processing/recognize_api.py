import aiohttp
import json

class RecognizeApi:
    def __init__(self, api_url='http://api:5000'):
        self.api_url = api_url
        self.headers = {'Content-type': 'application/json'}

    async def _post_request(self, endpoint, data):
        async with aiohttp.request(
            method='POST', 
            url=f"{self.api_url}/{endpoint}", 
            data=json.dumps(data), 
            headers=self.headers
        ) as response:
            return await response.json()

    async def fetch_material(self, image_url):
        return await self._post_request('detect_frame_material', {'url': image_url})

    async def fetch_tag(self, image_url):
        return await self._post_request('detect_frame_tag', {'url': image_url})

    async def fetch_type(self, image_url):
        return await self._post_request('detect_frame_type', {'url': image_url})
