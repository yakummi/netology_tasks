FROM python:3.10.0-alpine

WORKDIR usr/src/app

RUN apk install \ 
	&& apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY project/requirements.txt ust/src/app/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r usr/src/app/requirements.txt

COPY project usr/src/app
