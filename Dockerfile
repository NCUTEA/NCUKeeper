FROM python:3-alpine

LABEL MAINTAINER="NoCLin"

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r ./requirements.txt -i https://pypi.doubanio.com/simple/

ENTRYPOINT ["python","NCUKeeper.py"]
