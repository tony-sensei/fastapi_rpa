# FastAPI RPA

This repository contains a Robotic Process Automation (RPA) project that automatically opens Google Chrome, navigates to youtube.com, takes a screenshot of the page, and returns a JSON object containing all the texts on the screenshot along with their coordinates.

The project uses FastAPI for creating the web application, and several other libraries for automation and image processing tasks.

## Requirements

- Python 3.10.5
- MacOS (Currently, this project only works on MacOS)
- Google Chrome browser installed

## Installation

1. Clone this repository:
 
 ```
git clone https://github.com/tony-sensei/fastapi_rpa.git
cd fastapi_rpa

 ```

2. Create a virtual environment and activate it:

 ```
python3 -m venv env
source env/bin/activate

 ```

3. Install the required packages:

```
pip install -r requirements.txt

```

## Usage

1. Start the FastAPI application:

```
uvicorn main:app --reload

```

2. In another terminal, run the automation script:

```
python3 automation.py

```




