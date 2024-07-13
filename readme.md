# World Cup Predictor

## Synopsis
The goal of our project is to develop a predictive model for the FIFA World Cup outcomes using a large dataset of international football matches. This project aims to leverage data science techniques learned in class such as single/multiple linear regression, classification, and bagging to analyze historical match data and predict the outcomes of future matches.

## Team Members: 
| Bryan Quintero | Scott Willard | Jayden McKenna | Ernesto Rendon |
| :------------: | :-----------: | :------------: | :------------: |
|    48344993    |    44868436   |    80364767    |    94109996    |

## Usage

### 1. Clone the repo

### 2. Install dependencies
`pip install pymongo dnspython python-dotenv`

### 3. Set Up Environment Variables
Create a `.env` file in the root directory of your project. This file will contain your MongoDB connection credentials. Use example.env as a template to create `.env`

Replace `your_username` and `your_password` with your actual MongoDB credentials. The code in the `worldcup.ipynb` will pull in these variables from the `.env` file automatically.

### 4. Use the Jupyter notebook
After creating and modifying the `.env` file accordingly, you'll be able to use the MongoDB and query it as normal. Some example code is included there for testing; simply run the code in the cell to try it out.




