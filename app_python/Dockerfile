FROM python:3
LABEL maintainer="a.gorb@innopolis.university"

WORKDIR /app_python
COPY . /app_python

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python3", "main.py"]