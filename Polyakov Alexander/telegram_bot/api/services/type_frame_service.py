from lib.image_fetcher import ImageFetcher
from lib.image_resizer import ImageResizer
from predictors.glasses_checker import GlassesChecker
from predictors.type_predictor import TypePredictor

class TypeFrameService:
  def __init__(self, glasses_model, frame_model):
    self.glasses_find_model = glasses_model
    self.frame_model = frame_model
    self.resizer = ImageResizer()

  def call(self, image_url):
    image_fetcher = ImageFetcher(image_url)
    image = image_fetcher.fetch()
    
    check_glasses_img = self.resizer.resize_for_check(image, (120, 120))
    checker = GlassesChecker(self.glasses_find_model)
    result = checker.predict_threshold(check_glasses_img)

    if result == 1:
      frame_image = self.resizer.resize_for_type(image, (224, 224))
      frame_type_predictor = TypePredictor(self.frame_model)
      predict = frame_type_predictor.predict(frame_image)

      return predict
    else:
      return 'not_glasses'
