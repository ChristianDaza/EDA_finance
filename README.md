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

Once cloned, use the command line to navigate to the repository. Then move to the SRC folder and open the EDA.ipynb notebook and Analysis.ipynb.

The EDA.ipynb notebook relays on:
- db.utils.py (class RDSDatabaseConnector) to extract and save the SQL data store in AWS.
- pre_processing.py (class DataTransform) to alter columns and values of the dataframe.
- extract_info.py (class DataFrameInfo) helps to undertand the data such as the shape of the dataframe, missing values, skewness, descriptic statistics and outliers.
- plot.py (class Plotter) allows the user to create visualisations for the data based on the seaborn Python library.

Also, this notebook is broken into two main sections:

Database: 
- Extracting and saving the finance data form AWSRDS.

Preprocessing: 
-  Cirrecting data types: convert the columns into their correct data type
- missing values: remove and impute missing values
- Skewness: cpply transformations on skewed columns
- Outliers: remove outliers
- Correlation: remove overly correlated columns

After removing and imputing values the dataframe was saved (impute_loan_payments) and used for the remainign three tasks in the precossing section, since skew transformations will alter the original value of the data which will then affect interpretation in the analysis section.

The Analysis.ipynb has four sections:
- Calculating the current state of the loan
- Calculating loss
- Calculating possible loss
- Indicators of loss




## Main Featues

- Have classes for extracting data from the cloud, transforming, extracting information and visualisation of data.

    

## Licence
[MIT](https://github.com/ChristianDaza/Hangman/blob/main/LICENSE)

## Contact Information
- Christian
- ch.arenasdaza@gmail.com
- [GitHub](https://github.com/ChristianDaza)