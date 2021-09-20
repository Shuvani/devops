FROM python:3-slim
LABEL maintainer="a.gorb@innopolis.university"

RUN useradd user
USER user
WORKDIR /tmp

COPY ./requirements.txt /tmp
RUN pip install --target=/tmp --no-cache-dir -r /tmp/requirements.txt
COPY . /tmp

EXPOSE 8000
CMD ["python3", "main.py"]
