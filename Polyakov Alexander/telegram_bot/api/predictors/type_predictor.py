import numpy as np

class TypePredictor:
  LABELS = ["line", "rim", "sleeve"]

  def __init__(self, model):
    self.model = model
  
  def predict(self, image):
    predictions = self.model.predict(image)
    label_idx = np.argmax(predictions, axis=1)[0]
    return self.LABELS[label_idx]
