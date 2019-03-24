FROM python:3.7.1-slim-stretch

COPY codes/requirement_Keras.txt .
RUN pip install -r requirement_Keras.txt

COPY codes .
COPY bpemb_pretrained_cached /root/.cache/bpemb/en

CMD python my_waitress_live.py
