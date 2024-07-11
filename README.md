# EDA_finance
  
Exploratory data analysis fo financial loan data.

## Description
 
EDA_finance is a Python based data analytics project, in which data was extracted, pre_processed, visualise and analysis using a variety to obtained valueble information. The aim of this project was to apply the knowledge and skills gain in the AWS, SQL and Python EDA modules of AiCore to gain more experience. From this experience I leanerd that manipulating data such normalising distribution or removing outlier cannot be solely done using visualisation or statistical test, it also requires a deep understanding of the data itself and human judgement.

## Table of content

- [Description](#Description)
- [Intallation](#Intallation)
- [Usage](#Usage)
- [Main Features](#Main_Features)
- [Lincence](#Licence)
- [Contact Information](#Contact_information)


## Installation

 The source of this code is currently hosted at: https://github.com/ChristianDaza/EDA_finance.git

Clone this git repository into your machine using the following code:
```
git clone https://github.com/ChristianDaza/EDA_finance.git
```


## Usage

Once cloned, use the command line to navigate to the repository. This project is divided into two jupiter notebooks in the SRC folder: EDA.ipynb and Analysis.ipynb. First run the cells in EDA.ipynb and then Analysis.ipynb beacuse the analysis notebook relays on the cleaned datafrom the EDA notebook.

The EDA.ipynb (Exploratory data analys), which is broken into sections:
Database: 
- Extracting and saving the finance data form AWS RDS.

Preprocessing: 
- Correcting data types: convert the columns into their correct data type
- missing values: remove and impute missing values
- Skewness: check for skewness and apply transformations correct it.
- Outliers: detect and remove outliers
- Correlation: detect and remove overly correlated columns

After removing and imputing values the dataframe was saved (impute_loan_payments) for the analysis section, since skew transformations will alter the original value of the data which will then affect interpretation.

The Analysis.ipynb has four sections:
- Calculating the current state of the loans: how much money from the loans had been recovered and hwo much will the company expect to gain in the next 6 months
- Calculating loss: the revenue lost from loans that had been charged off
- Calculating possible loss: the possible revenue loss if the loans with late status will become charged off loans.
- Indicators of loss: analysis which columns in the dataframe can predict if a late loan will become a charged off loan.


## Main Featues

-  Class RDSDatabaseConnector (db.utils.py) extracts and save the SQL data store in AWS.
-  Class RDSDatabaseConnector (db.utils.py) displays all the tables in the cloud database and allow the user to chose wich one will be download.
-  Class DataTransform (pre_processing.py) transforms columns and values of the dataframe.
-  Class DataFrameInfo (extract_info.py) helps to undertand the data such as the shape of the dataframe, missing values, skewness, descriptic statistics and outliers.
-  Class Plotter (plot.py) allows the user to create visualisations for the data based on the seaborn Python library.

## Licence
[MIT](https://github.com/ChristianDaza/Hangman/blob/main/LICENSE)

## Contact Information
- Christian
- ch.arenasdaza@gmail.com
- [GitHub](https://github.com/ChristianDaza)