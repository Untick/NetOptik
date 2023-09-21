from config import pm

class MaterialPredict:
    def __init__(self, file_path, recognizer):
        self.file_path = file_path
        self.recognizer = recognizer

    async def predict(self):
        res = await self.recognizer.fetch_material(self.file_path)
        result = res.get('result', 'unknown')

        if result == 'plastic':
            return pm.t('predict.material.is_plastic')
        elif result == 'metall':
            return pm.t('predict.material.is_metall')
        elif result == 'not_glasses':
            return pm.t('predict.is_not_glasses')
        else:
            return pm.t('predict.is_unknown')
