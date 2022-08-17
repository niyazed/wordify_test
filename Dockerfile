FROM python:3.9

WORKDIR /workspace

COPY ./requirements.txt /workspace/requirements.txt

# RUN apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig

RUN pip install --no-cache-dir --upgrade -r /workspace/requirements.txt

COPY . /workspace

EXPOSE 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]