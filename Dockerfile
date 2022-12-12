FROM python:3.8


RUN pip install cmake 
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
#COPY ./apps /main
WORKDIR /main