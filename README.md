# Python API-Automation 
Hybrid Custom Framework to Test the REST APIs


### Tech Stack
1. Python 3.11
2. Requests - HTTP Requests
3. PyTest - Testing Framework
4. Reporting - Allure Report, PyTest HTML
5. Test Data - CSV, Excel, JSON
6. Parallel Execution - x distribute

## How to Install Packages
"pip install requests pytest pytest-html faker allure-pytest jsonschema"

## To Freeze your Package version
pip freeze > requirements.txt

## To Install te Freeze Version
"pip install -r requirements.txt" <<<<<<< HEAD

## How to run your Testcase Parallel
pip install pytest-xdist

pytest -n auto tests/integration_test/test_create_booking.py -s -v 

##To Work with the Excel- read write
pip install openpyxl

## To Install faker for random data
pip install faker

from faker import Faker
faker=Faker()
faker.first_name()

## Install .env package for secured environment
pip install python-dotenv

from dotenv import load_dotenv
import os

## To work wit JSON Schema
pip install jsonschema

from jsonschema import validate
from jsonschema.exceptions import ValidationError