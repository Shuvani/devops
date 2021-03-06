# Moscow time

![example workflow](https://github.com/Shuvani/devops/actions/workflows/CI-CD.yaml/badge.svg)

## About the project
This is the web application which shows the time at which you visited the page last

## Built with
- python
- Sanic - python web server and web framework

## Getting started by hands
To get a local copy up and running follow these simple steps:
clone the repo
```
cd devops/app_python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Testing
```
app_python$ pytest test.py
```

## Usage
```
app_python$ python3 main.py
```
open http://0.0.0.0:8000/v12.4.1/ in the browser

## Getting started with Docker-compose
```
app_python$ docker-compose up
```
open http://0.0.0.0:8000/v12.4.1/ in the browser

## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## Contact
Anna Gorb - a.gorb@innopolis.university
