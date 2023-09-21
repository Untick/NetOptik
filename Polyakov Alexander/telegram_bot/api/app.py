from flask import Flask, request, make_response, jsonify
from tensorflow.keras.models import load_model
from ultralytics import YOLO
from services.glasses_frame_service import GlassesFrameService
from services.type_frame_service import TypeFrameService
from services.glasses_tag_service import GlassesTagService

app = Flask(__name__)
glasses_find = load_model("ai_models/best_autoencoder_v2.h5")
frame_materialt_model = load_model("ai_models/best_model_gen_8_2.h5")
frame_type_model = load_model('ai_models/best_model_EfficientNetB3_val_accuracy_scratch.h5')
tag_model = YOLO('ai_models/yolo_tag.pt')

# Main page 
@app.route("/")
def hello():
  return "OK"

@app.route('/detect_frame_material', methods=['POST'])
def detect_frame_material():
  if 'url' in request.json:
    image_url = request.json['url']
    service = GlassesFrameService(glasses_find, frame_materialt_model)
    result = service.call(image_url)

    return make_response(jsonify({'result': result}), 200)

@app.route('/detect_frame_type', methods=['POST'])
def detect_frame_type():
  if 'url' in request.json:
    image_url = request.json['url']
    service = TypeFrameService(glasses_find, frame_type_model)
    result = service.call(image_url)

    return make_response(jsonify({'result': result}), 200)

@app.route('/detect_frame_tag', methods=['POST'])
def detect_frame_tag():
  if 'url' in request.json:
    image_url = request.json['url']
    result = GlassesTagService(tag_model).call(image_url)

    return make_response(jsonify({'result': result}), 200)

if __name__ == '__main__':
    app.run(debug=True)