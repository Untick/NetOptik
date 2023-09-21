from processing.recognize_api import RecognizeApi
from predict.material_predict import MaterialPredict
from predict.tag_predict import TagPredict
from predict.type_predict import TypePredict

class Predictor:
    def __init__(self, file_path, last_button):
        self.file_path = file_path
        self.last_button = last_button
        self.recognizer = RecognizeApi()

    async def predict(self):
        if self.last_button == "material":
            predictor = MaterialPredict(self.file_path, self.recognizer)
        elif self.last_button == "tag":
            predictor = TagPredict(self.file_path, self.recognizer)
        elif self.last_button == "type":
            predictor = TypePredict(self.file_path, self.recognizer)
        else:
            raise ValueError("Unknown button type")

        return await predictor.predict()
