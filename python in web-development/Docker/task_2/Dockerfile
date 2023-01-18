FROM python:3.11

COPY smart_home/requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

COPY smart_home /app

EXPOSE 6666

WORKDIR app

CMD ['python3', 'manage.py', 'runserver', '0.0.0.0:6666']

