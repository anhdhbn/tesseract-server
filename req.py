import requests
import base64

with open("test.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

req = requests.post("http://127.0.0.1:5000/api/ocr", json={
    "imagestr": encoded_string.decode() 
})

print(req.json())