# Goodness-of-fit Function Used in Python
## Introduction
Such as evapotranspiration and leaf area index can be estimated via trained machine learning methods when the ground measurements are available. A variety of metrics can tell us how the performance of the machine-learning model is. Based on my current experience and considering that python is popular since it could be combined with other software such as ArcGIS, this project is aiming at providing a python function package and also basic concepts of each goodness-of-fit methods in order to provide a potential way to compare the results from different research paths and to save time to look for the details about each goodness-of-fit method. This repository is organized to show the python package in the first part, followed by the description for each method, and one example shows at the end.
The symbols used in this paper include:
n: the number of observations
O: it stands for the ground observation
O ̅: the average of ground observations
O_i: ground observations
E: it stands for the estimation gained via ML methods
E ̅: the average of estimations gained from ML models
E_i: estimated value via ML models
