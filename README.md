# django-stock-trades-api

This repo is created to show case a stock trades API site based on Django Restframework.

## Setup

run this first

```sh
./setup.sh
```

then browse this url

- http://localhost:8000/trades/
- http://localhost:8000/trades/users
- http://localhost:8000/trades/1
- http://localhost:8000/trades/users/1/


## Testing
At the moment, only test inside http-small.json file is run.

```sh
python manage.py test
```

Pls check the output file unit.xml at root folder location.



