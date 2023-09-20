import numpy as np

class MaterialPredictor:
  def __init__(self, model):
    self.model = model
  
  def predict(self, image):
    pred = self.model.predict(image)
    return 'plastic' if pred[0][0] == 1.0 else 'metall'
