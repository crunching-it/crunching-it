# Crunching it

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/crunching-it/crunching-it/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/crunching-it/crunching-it/?branch=master)
[![Code Coverage](https://scrutinizer-ci.com/g/crunching-it/crunching-it/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/crunching-it/crunching-it/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/crunching-it/crunching-it/badges/build.png?b=master)](https://scrutinizer-ci.com/g/crunching-it/crunching-it/build-status/master)

## How do I set up my development environment?

This is the process almost from scratch, assuming you're on a Mac and have installed Homebrew already.

1. Install Python: `brew install python3`
2. Upgrade package management tools: `pip3 install --upgrade pip setuptools wheel virtualenv`
4. Prepare to create you virtual environment: `mkdir ~/.virtualenvs`
5. Create your virtual environment: `python3 -m venv ~/.virtualenvs/crunching-it`
6. Activate your virtual environment: `source ~/.virtualenvs/crunching-it/bin/activate`
7. Clone the repository: `git clone git@github.com:crunching-it/crunching-it.git crunching_it`
8. Navigate into the project: `cd crunching_it`
9. Install the required packages: `pip install -r requirements.txt`
9. Create your local settings module: `cp local_settings.py.dist local_settings.py`
9. Add a secret key to `local_settings.SECRET_KEY`
10. Start the development webserver: `python manage.py runserver`
11. Visit [http://localhost:8000/](http://localhost:8000/).

To _deactivate_ (exit) your virtual environment, use the `deactivate` command.
