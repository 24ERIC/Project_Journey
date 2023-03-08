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

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 