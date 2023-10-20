# Django Training Project

A simple training project for learning the basics of Django

## Installation

First, [install pyenv](https://github.com/pyenv/pyenv#installation). Then, create your python virtual environment:
```bash
pyenv local 3.8.12
```
```bash
python -m venv venv
```
```bash
source venv/bin/activate
```

Now, install the dependendies in `requirements.txt`:
```bash
pip install -r requirements.txt
```

Next, apply all migrations:
```bash
python manage.py migrate
```

Finally, run your server:
```bash
python manage.py runserver
```
