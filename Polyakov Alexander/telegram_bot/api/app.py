from flask import Flask, request, make_response, jsonify
from frame_material import FrameMaterial
from tensorflow.keras.models import load_model

app = Flask(__name__)
frame_materialt_model = load_model("models/best_model_gen_8_2.h5")

def interpret_result_material(res):
    if res == [[1.0]]:
        return 'plastic'
    elif res == [[0.0]]:
        return 'metall'
    else:
        return 'unknown'

# стартовая страница
@app.route("/")
def hello():
    return "OK"

@app.route('/detect_frame_material', methods=['POST'])
def detect_frame_material():
    if 'url' in request.json:
        image_url = request.json['url']
        # Predict service
        material_predictor = FrameMaterial(frame_materialt_model, image_url)
        predict = material_predictor.fetch_and_predict()
        result = interpret_result_material(predict)
    return make_response(jsonify({'result': result}), 200)

if __name__ == '__main__':
    app.run(debug=True)