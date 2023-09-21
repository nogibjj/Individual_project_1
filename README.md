[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Format](https://github.com/nogibjj/Individual_project_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Individual_project_1/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/Individual_project_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Individual_project_1/actions/workflows/install.yml)
[![Lint](https://github.com/nogibjj/Individual_project_1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Individual_project_1/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/Individual_project_1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Individual_project_1/actions/workflows/test.yml)

## Individual Project 1: Continuous Integration using GitHub Actions with RUFF linter

## Summary
This is indivudual project for IDS706 Data Engineering. In the project, we created a python script, along with a jupyter notebook script to produce some descriptive statistics for a [dataset](https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv). The goal is to achieve automatic continous integration on Github including instaling, linting, testing and formating.

## Project Structure
* `MakeFile` contains automatic processes for installing, linting, testing and formating
* `requirements.txt` includes pinned python packages used in this project
* `descriptive_script.py` includes python script code for producing descriptive statistics
* `notebook_descriptive` includes python script and markdowns for descriptive statistics
* `lib.py` stores all the necessary methods/functions shared between `descriptive_script.py` and `notebook_descriptive`
* `test_lib.py` and `test_script.py` test codes in script and lib using ruff 

## Video Demo
Watch the [video](https://youtu.be/reEaAqqZ6xo) to walk through the project. 



