from sklearn.metrics import mean_squared_error

class GlassesChecker:
  def __init__(self, model, image_size=120*120*3, threshold=0.003):
    self.autoencoder = model
    self.image_size = image_size
    self.threshold = threshold

  def predict_error(self, image):
    """Прогнозирование и вычисление ошибки для заданного изображения."""
    pred = self.autoencoder.predict(image.reshape(1, *image.shape))
    # Подсчет ошибки
    err = mean_squared_error(image.reshape(-1), pred.reshape(-1))
    return err

  def predict_threshold(self, image):
    """Возвращает 1, если ошибка превышает порог, иначе 0."""

    error = self.predict_error(image)
    if error > self.threshold:
      return 0
    else:
      return 1
