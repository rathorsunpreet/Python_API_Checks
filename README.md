# Reqres Python API Checks

Project performs API Testing of the site [reqres.in](https://reqres.in/) using Pytest and Requests.

## Installation

Download the package from [Github](https://github.com/rathorsunpreet/Python_API_Checks) and unzip it.

```console
# Create virtual environment
python -m venv --prompt . .venv

# Activate virtual environment
# Linux / MacOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate.bat

# Upgrade pip
python -m pip install --upgrade pip

# Installs dependencies
pip install -r requirements.txt 
```
## Usage

```console
# To execute the tests
pytest

# To execute the tests visually
pytest -v

# To generate a report after executing tests
pytest -v --html=reports/report.html
```

## Upgrade
To upgrade the dependencies, update the version numbers in __requirements.in__ and then in the virtual environment, use the following:
```console
# Updating dependencies
pip-compile -r
```
and then follow the steps to install dependencies from the Install Section.

## License

[MIT](https://choosealicense.com/licenses/mit/)
