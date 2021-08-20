FROM python:3
LABEL maintainer="a.gorb@innopolis.university"

WORKDIR /app_python
COPY requirements.txt /app_python/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app_python

EXPOSE 8000

ENTRYPOINT ["python3", "main.py"]