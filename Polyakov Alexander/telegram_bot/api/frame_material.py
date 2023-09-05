from image_fetcher import ImageFetcher
import numpy as np
from PIL import Image

class FrameMaterial:
    def __init__(self, model, url):
        self.url = url
        self.image_fetcher = ImageFetcher(self.url)
        self.model = model
        self.image_size = (200, 120)
    
    def fetch_and_predict(self):
        image = self.image_fetcher.fetch()
        if image is not None:
            return self.predict(image)
        else:
            return "Не удалось получить изображение."
    
    def predict(self, image):
        resized_image = self.image_resize(image)
        result = self.model.predict(resized_image)
        return result.tolist()

    def image_resize(self, image):
        image_pil = Image.fromarray(np.uint8(image))
        resized_image_pil = image_pil.resize(self.image_size, Image.LANCZOS)
        resized_image = np.array(resized_image_pil)
        image_batch = np.expand_dims(resized_image, axis=0)

        return image_batch
