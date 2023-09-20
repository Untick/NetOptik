from config import pm
class TagPredict:
  def __init__(self, file_path, recognizer):
    self.file_path = file_path
    self.recognizer = recognizer

  async def predict(self):
    res = await self.recognizer.fetch_tag(self.file_path)
    result = res.get('result', 'unknown')

    if result != "unknown":
      return pm.t('predict.tag.result', **result)
    else:
      return pm.t('predict.tag.is_unknown')
