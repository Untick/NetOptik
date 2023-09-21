from config import pm
class TypePredict:
  def __init__(self, file_path, recognizer):
    self.file_path = file_path
    self.recognizer = recognizer

  async def predict(self):
    res = await self.recognizer.fetch_type(self.file_path)

    result = res.get('result', 'unknown')

    if result == 'line':
        return pm.t('predict.type.is_line')
    elif result == 'rim':
        return pm.t('predict.type.is_rim')
    elif result == 'sleeve':
        return pm.t('predict.type.is_sleeve')
    elif result == 'not_glasses':
        return pm.t('predict.is_not_glasses')
    else:
        return pm.t('predict.is_unknown')
