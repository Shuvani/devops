# PRODUCTION READY FRAMEWORK
This application was written with **Sanic** - python web server and web framework
- allows to use async/await which makes the process non-blocking and fast
- easy to build, expand and scale
- is production ready
- lightweight and without many build-in features

# BEST PRACTICES
- I took **Sanic** because simplicity is better than functionality
- well-structured code
```
only several files that perform different functions
- main.py with the code
- test.py with the tests
- html file in the templates folder to display UI
```
- setup.py
- README
- requirements.txt
- comments and documentation
- proper namings
```
function and variables in lower_case_with_underscores
```
- PEP8 checks with the **flake8** library - combo linter
```
app_python$ flake8 main.py
app_python$ flake8 test.py
```
- unit tests
```
app_python$ pytest test.py
```
- long descriptive names for tests
- tests are isolated
- versioning in the url
- **PyPI** use instead of the self made code - code moduling
- **venv** to separate the environments
- formatting was checked with the **black** and **isort** libraries
```
app_python$ black main.py
app_python$ black test.py
app_python$ isort .
```
- **CSS** usage because beautiful is better than ugly

# MARKDOWN LINTER
I installed *pymarkdownlint*
'''
markdownlint PYTHON.md
'''