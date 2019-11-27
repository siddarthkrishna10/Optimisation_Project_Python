# Optimisation in Data Science Assignment
An Optimisation Project in Python. Studying trends in Football Transfers and building a regression model to predict the market value of players.

## Part I 
**Goal:** To see and understand the trend of how much clubs have been paying over the market value for players over 14 seasons.

### Files for PART I:
- _Transfers.csv_ - The CSV file that contains the full Kaggle dataset.
- _Calculating_Difference.py_ - The python file that calculates the Difference metric and the Average Difference.
  - _Mean_Table.csv_ is created.
  - _Line_Graph.png_ - Image of the line graph
- _Plot_Difference.py_ - Python file where the line graph for Average Difference is plotted.

### Packages for PART 1:
- _import pandas as pd_
- _import numpy as np_
- _import matplotlib.pyplot as plt_

## Part II
**Goal:** To split, train the dataset and apply Linear Regression in the hopes of creating a accurate model to predict the Market Value of players in the coming seasons.

### Files for PART II:
- _Transfers.csv_ - The CSV file that contains the full Kaggle dataset.
- _Plot_Regression.py_ - Python file for creating the full Linear Regression model.
  - _Actual_Predicted.csv_ is created.
  - _Linear_Regression.png_ - Image of the linear regression model and scatter plot

### Packages for PART II:
- _import numpy as np_
- _import pandas as pd_
- _import matplotlib.pyplot as plt_
- _from sklearn.model_selection import train_test_split_
- _from sklearn.linear_model import LinearRegression_
- _from sklearn import metrics_
