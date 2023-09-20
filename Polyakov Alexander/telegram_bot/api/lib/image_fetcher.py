from io import BytesIO
import requests
import numpy as np
from PIL import Image

class ImageFetcher:
  def __init__(self, url):
    self.url = url

  def fetch(self):
    response = requests.get(self.url, stream=True)
    if response.status_code == 200:
      img = np.asarray(Image.open(BytesIO(response.content)).convert('RGB'))
      return img
    else:
      return None
