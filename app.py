# app.py
from flask import Flask, request, jsonify
from PIL import Image
import cv2
import numpy as np
import pytesseract
import base64
import io

app = Flask(__name__)

def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

@app.route('/api/ocr', methods=['POST'])
def ocr():
    image_str = request.get_json()['imagestr']
    image = stringToRGB(image_str)
    result = pytesseract.image_to_string(image , lang = 'vie')
    return {
        'result': result
    }

@app.route('/')
def index():
    return "<h1>OCR api</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)