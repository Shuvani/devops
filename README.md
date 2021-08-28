# Moscow time

## About the project
This is the web application which shows the current Moscow time when you reload the page

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

## Usage
```
python3 main.py
```
open http://0.0.0.0:8000/v2.0.6/ in the browser

## Getting started with Docker
```
docker pull shuvani/moscow_time:v2.0.6 // to update the version
docker run -p 8000:8000 shuvani/moscow_time:v2.0.6
```
open http://0.0.0.0:8000/v2.0.6/ in the browser

## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## Workflows:
Before push or pull request in the main branch the code passes testing procedures

![example workflow](https://github.com/Shuvani/devops/actions/workflows/publish.yaml/badge.svg)

Before push in the release branches the application is published on the DockerHub

![example workflow](https://github.com/Shuvani/devops/actions/workflows/testing.yaml/badge.svg)

## Contact
Anna Gorb - a.gorb@innopolis.university
