FROM python:3.6
RUN apt-get update && apt-get install tesseract-ocr tesseract-ocr-vie -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
