from lib.image_fetcher import ImageFetcher
from lib.image_resizer import ImageResizer
from predictors.glasses_tag import GlassesTag
from db.tags_repo import TagsRepo

class GlassesTagService:
  def __init__(self, model):
    self.model = model
    self.resizer = ImageResizer()

  def call(self, image_url):
    image_fetcher = ImageFetcher(image_url)
    image = image_fetcher.fetch()
  
    resized_iamge = self.resizer.resize_for_tag(image, (640, 480))
    
    predictor = GlassesTag(self.model, resized_iamge)
    search_tag = predictor.text_tag()
    
    result = TagsRepo().find_most_relevant(search_tag)

    return result