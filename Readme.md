# Parser:
Python parser to scrap product info from pages

## Installation:
Install Python3  
Install Firefox browser and Geckodriver
Download pip: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`  
Install pip: `python3 get-pip.py` (MacOS) or with `sudo apt-get install pip` (Linux)  
Run `pip3 install -r requirements.txt` from project directory  
Rename `dist.env `to `.env` or set env vars with values  

## Run form console:
Open terminal window, and from project directory run: `python3 command.py`
List of products with details will be returned

## Tests:
From new terminal window execute tests with `python3 -m unittest tests.ProductScraperTest`  

## Tests Code Coverage:
From new terminal window execute tests with `coverage run --source=. tests.py `  
Generate html report with: `coverage html`  
Erase current coverage: `coverage erase`  

## Run in env
To create env run: `python3 -m venv env`
Activate env with: `source env/bin/activate` an d run all of above commands from env