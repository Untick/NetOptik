FROM python:3.9

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev libgl1-mesa-glx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
