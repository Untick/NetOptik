import pytesseract

class GlassesTag:
  def __init__(self, model, image_file):
    self.image = image_file
    self.model = model

  def image_tag(self):
    predict_results = self.model.predict(self.image, max_det=1)
    images = self.crop_image_using_bboxes(self.image, predict_results[0].boxes.data)
    return images[0]

  def text_tag(self):
    img = self.image_tag()
    result = pytesseract.image_to_string(img)
    return result

  def crop_image_using_bboxes(self, image, boxes):
    cropped_images = []

    for box in boxes:
      x_min, y_min, x_max, y_max = box[:4]
      cropped_image = image[int(y_min):int(y_max), int(x_min):int(x_max)]
      cropped_images.append(cropped_image)

    return cropped_images
