FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /urlshort
WORKDIR /urlshort
ADD requirements.txt /urlshort/
RUN pip install -r requirements.txt
ADD . /urlshort/