from PIL import Image
import numpy as np

class ImageResizer:
  def _resize_image(self, image, image_size):
    image_pil = Image.fromarray(np.uint8(image))
    return image_pil.resize(image_size, Image.LANCZOS)
  
  def _convert_to_array(self, resized_image_pil, normalize=False):
    resized_image = np.array(resized_image_pil)
    if normalize:
      resized_image = resized_image / 255.0
    return resized_image
  
  def resize(self, image, image_size):
    resized_image_pil = self._resize_image(image, image_size)
    resized_image = self._convert_to_array(resized_image_pil)
    return np.expand_dims(resized_image, axis=0)

  def resize_for_check(self, image, image_size):
    resized_image_pil = self._resize_image(image, image_size)
    return self._convert_to_array(resized_image_pil, normalize=True)

  def resize_for_type(self, image, image_size):
    resized_image_pil = self._resize_image(image, image_size)
    resized_image = self._convert_to_array(resized_image_pil, normalize=True)
    return np.expand_dims(resized_image, axis=0)
  
  def resize_for_tag(self, image, image_size):
    resized_image_pil = self._resize_image(image, image_size)
    resized_image = self._convert_to_array(resized_image_pil)
    return resized_image