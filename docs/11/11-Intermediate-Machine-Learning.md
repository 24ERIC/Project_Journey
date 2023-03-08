# 11-Intermediate-Machine-Learning.md

# Note

- If you have some background in machine learning and you'd like to learn how to quickly improve the quality of your models, you're in the right place! In this course, you will accelerate your machine learning expertise by learning how to:


    tackle data types often found in real-world datasets (missing values, categorical variables),
    design pipelines to improve the quality of your machine learning code,
    use advanced techniques for model validation (cross-validation),
    build state-of-the-art models that are widely used to win Kaggle competitions (XGBoost), and
    avoid common and important data science mistakes (leakage).

- Along the way, you'll apply your knowledge by completing a hands-on exercise with real-world data for each new topic. The hands-on exercises use data from the Housing Prices Competition for Kaggle Learn Users, where you'll use 79 different explanatory variables (such as the type of roof, number of bedrooms, and number of bathrooms) to predict home prices. You'll measure your progress by submitting predictions to this competition and watching your position rise on the leaderboard!
- 

This notebook is an exercise in the Intermediate Machine Learning course. You can reference the tutorial at this link.

As a warm-up, you'll review some machine learning fundamentals and submit your initial results to a Kaggle competition.
Setup

The questions below will give you feedback on your work. Run the following cell to set up the feedback system.
[1]:

# Set up code checking

import os

if not os.path.exists("../input/train.csv"):

    os.symlink("../input/home-data-for-ml-course/train.csv", "../input/train.csv")  

    os.symlink("../input/home-data-for-ml-course/test.csv", "../input/test.csv")  

from learntools.core import binder

binder.bind(globals())

from learntools.ml_intermediate.ex1 import *

print("Setup Complete")

Setup Complete

You will work with data from the Housing Prices Competition for Kaggle Learn Users to predict home prices in Iowa using 79 explanatory variables describing (almost) every aspect of the homes.

Ames Housing dataset image

Run the next code cell without changes to load the training and validation features in X_train and X_valid, along with the prediction targets in y_train and y_valid. The test features are loaded in X_test. (If you need to review features and prediction targets, please check out this short tutorial. To read about model validation, look here. Alternatively, if you'd prefer to look through a full course to review all of these topics, start here.)
[2]:

import pandas as pd

from sklearn.model_selection import train_test_split

​

# Read the data

X_full = pd.read_csv('../input/train.csv', index_col='Id')

X_test_full = pd.read_csv('../input/test.csv', index_col='Id')

​

# Obtain target and predictors

y = X_full.SalePrice

features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = X_full[features].copy()

X_test = X_test_full[features].copy()

​

# Break off validation set from training data

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,

                                                      random_state=0)

Use the next cell to print the first several rows of the data. It's a nice way to get an overview of the data you will use in your price prediction model.
[3]:

X_train.head()

	LotArea 	YearBuilt 	1stFlrSF 	2ndFlrSF 	FullBath 	BedroomAbvGr 	TotRmsAbvGrd
Id 							
619 	11694 	2007 	1828 	0 	2 	3 	9
871 	6600 	1962 	894 	0 	1 	2 	5
93 	13360 	1921 	964 	0 	1 	2 	5
818 	13265 	2002 	1689 	0 	2 	3 	7
303 	13704 	2001 	1541 	0 	2 	3 	6

The next code cell defines five different random forest models. Run this code cell without changes. (To review random forests, look here.)
[4]:

from sklearn.ensemble import RandomForestRegressor

​

# Define the models

model_1 = RandomForestRegressor(n_estimators=50, random_state=0)

model_2 = RandomForestRegressor(n_estimators=100, random_state=0)

model_3 = RandomForestRegressor(n_estimators=100, criterion='absolute_error', random_state=0)

model_4 = RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0)

model_5 = RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0)

​

models = [model_1, model_2, model_3, model_4, model_5]

To select the best model out of the five, we define a function score_model() below. This function returns the mean absolute error (MAE) from the validation set. Recall that the best model will obtain the lowest MAE. (To review mean absolute error, look here.)

Run the code cell without changes.
from sklearn.metrics import mean_absolute_error

# Function for comparing different models
def score_model(model, X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    model.fit(X_t, y_t)
    preds = model.predict(X_v)
    return mean_absolute_error(y_v, preds)

for i in range(0, len(models)):
    mae = score_model(models[i])
    print("Model %d MAE: %d" % (i+1, mae))
- 
- Step 1: Evaluate several models

Use the above results to fill in the line below. Which model is the best model? Your answer should be one of model_1, model_2, model_3, model_4, or model_5.

- # Fill in the best model
best_model = model_3

# Check your answer
step_1.check()
- 

In this tutorial, you will learn three approaches to dealing with missing values. Then you'll compare the effectiveness of these approaches on a real-world dataset.
Introduction

There are many ways data can end up with missing values. For example,

    A 2 bedroom house won't include a value for the size of a third bedroom.
    A survey respondent may choose not to share his income.

Most machine learning libraries (including scikit-learn) give an error if you try to build a model using data with missing values. So you'll need to choose one of the strategies below.

- 
- 1) A Simple Option: Drop Columns with Missing Values

The simplest option is to drop columns with missing values.
- 2) A Better Option: Imputation

Imputation fills in the missing values with some number. For instance, we can fill in the mean value along each column.
- 2) A Better Option: Imputation

Imputation fills in the missing values with some number. For instance, we can fill in the mean value along each column.
- Imputation is the standard approach, and it usually works well. However, imputed values may be systematically above or below their actual values (which weren't collected in the dataset). Or rows with missing values may be unique in some other way. In that case, your model would make better predictions by considering which values were originally missing.
- Example

In the example, we will work with the Melbourne Housing dataset. Our model will use information such as the number of rooms and land size to predict home price.

We won't focus on the data loading step. Instead, you can imagine you are at a point where you already have the training and validation data in X_train, X_valid, y_train, and y_valid.
- 
Define Function to Measure Quality of Each Approach

We define a function score_dataset() to compare different approaches to dealing with missing values. This function reports the mean absolute error (MAE) from a random forest model.

- 
Score from Approach 1 (Drop Columns with Missing Values)

Since we are working with both training and validation sets, we are careful to drop the same columns in both DataFrames.

- 
cols_with_missing = [col for col in X_train.columns
                     if X_train[col].isnull().any()]
- 
# Drop columns in training and validation data
reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)

- 
print("MAE from Approach 1 (Drop columns with missing values):")
print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))
- 
Score from Approach 2 (Imputation)

Next, we use SimpleImputer to replace missing values with the mean value along each column.

Although it's simple, filling in the mean value generally performs quite well (but this varies by dataset). While statisticians have experimented with more complex ways to determine imputed values (such as regression imputation, for instance), the complex strategies typically give no additional benefit once you plug the results into sophisticated machine learning models.

- from sklearn.impute import SimpleImputer
- 
# Imputation
my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

- 
# Imputation removed column names; put them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns
- 
print("MAE from Approach 2 (Imputation):")
print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))
- 

We see that Approach 2 has lower MAE than Approach 1, so Approach 2 performed better on this dataset.
Score from Approach 3 (An Extension to Imputation)

Next, we impute the missing values, while also keeping tr

# Make copy to avoid changing original data (when imputing)
X_train_plus = X_train.copy()
X_valid_plus = X_valid.copy()
ack of which values were imputed.
- uted
for col in cols_with_missing:
    X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
    X_valid_plus[col + '_was_missing'] = X_valid_plus[col].isnull()

- 
# Imputation
my_imputer = SimpleImputer()
imputed_X_train_plus = pd.DataFrame(my_imputer.fit_transform(X_train_plus))
imputed_X_valid_plus = pd.DataFrame(my_imputer.transform(X_valid_plus))

# Imputation removed column names; put them back
imputed_X_train_plus.columns = X_train_plus.columns
imputed_X_valid_plus.columns = X_valid_plus.columns

print("MAE from Approach 3 (An Extension to Imputation):")
print(score_dataset(imputed_X_train_plus, imputed_X_valid_plus, y_train, y_valid))
- 

MAE from Approach 3 (An Extension to Imputation):
178927.503183954

As we can see, Approach 3 performed slightly worse than Approach 2.
So, why did imputation perform better than dropping the columns?

The training data has 10864 rows and 12 columns, where three columns contain missing data. For each column, less than half of the entries are missing. Thus, dropping the columns removes a lot of useful information, and so it makes sense that imputation would perform better.

- # Shape of training data (num_rows, num_columns)
print(X_train.shape)

# Number of missing values in each column of training data
missing_val_count_by_column = (X_train.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])

(10864, 12)
Car               49
BuildingArea    5156
YearBuilt       4307
dtype: int64


- 
- 
- 
- 
- 