# Flask App: Create SaaS Software
An application to create SaaS-based software with Flask, Python, Docker, gunicorn, celery.

## Docker
### First time docker build
`docker-compose --build`

### Subsequent up Docker server
`docker-compose up`

### To stop Docker server
`docker-compose stop`

### To remove docker compose image
`docker-compose rm -f`

### To remove dangling docker image
`docker rmi -f $(docker images -qf dangling=true)`

### To check docker images
`docker images`


## Pytest
1. Create `tests` folder under resources folder.
2. In `conftest.py`, put all configuration decorators.
3. Write test cases with `assert` and `response`.

### Use docker to execute test
`docker-compose exec website py.test {path to test folder}`
- `website` is the label name from docker-compose file
- `py.test` is the command to execute
- `{path to test folder}`. For this case, it is `snakeeyes/tests`.

Example of response:
```
============================== test session starts ==============================
platform linux -- Python 3.7.5, pytest-5.1.0, py-1.8.1, pluggy-0.13.1
rootdir: /snakeeyes
plugins: cov-2.7.1
collected 4 items                                                               

snakeeyes/tests/page/test_views.py ....                                   [100%]

=============================== 4 passed in 0.36s ===============================
```

### Use docker check test coverage
`docker-compose exec website py.test --cov-report term-missing --cov snakeeyes`
- `term-missing` is to check the missing test

Example of response (should expect 100% coverage):
```
----------- coverage: platform linux, python 3.7.5-final-0 -----------
Name                                    Stmts   Miss  Cover   Missing
---------------------------------------------------------------------
snakeeyes/__init__.py                       0      0   100%
snakeeyes/app.py                           10      0   100%
snakeeyes/blueprints/__init__.py            0      0   100%
snakeeyes/blueprints/page/__init__.py       1      0   100%
snakeeyes/blueprints/page/views.py         11      0   100%
snakeeyes/tests/__init__.py                 0      0   100%
snakeeyes/tests/conftest.py                11      0   100%
snakeeyes/tests/page/__init__.py            0      0   100%
snakeeyes/tests/page/test_views.py         14      0   100%
---------------------------------------------------------------------
TOTAL                                      47      0   100%
```

### To run Flake8
`docker-compose exec website flake8 .`
`docker-compose exec website flake8 . --exclude __init__.py`
- Note: Remember to import page by adding `from snakeeyes.blueprints.page import page`