# World Cup Predictor

## Synopsis
The goal of our project is to develop a predictive model for the FIFA World Cup outcomes using a large dataset of international football matches. This project aims to leverage data science techniques learned in class such as single/multiple linear regression, classification, and bagging to analyze historical match data and predict the outcomes of future matches.

## Team Members: 
| Bryan Quintero | Scott Willard | Jayden McKenna | Ernesto Rendon |
| :------------: | :-----------: | :------------: | :------------: |
|    48344993    |    44868436   |    80364767    |    94109996    |

## Usage

### 1. Clone the repo
`gh repo clone ernestorendon/cap4770-finalproject`

### 2. Navigate to the project directory
`cd cap4770-finalproject`

### 3. Create and activate a Python virtual environment using Pipenv
```
pip install pipenv
pipenv install
```

### 4. Run the setup script
`./setup.sh`

### 5. Input MongoDB Credentials
Replace `your_username` and `your_password` in the `.env` file with your actual MongoDB credentials. 

The notebooks will pull in these variables from the `.env` file automatically.

### 6. Use the Jupyter notebook
After creating and modifying the `.env` file accordingly, you'll be able to use the MongoDB and query it as normal. 

Some example code is included there for testing; simply run the code in the cell to try it out.
