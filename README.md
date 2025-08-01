[![DOI](https://zenodo.org/badge/290397319.svg)](https://doi.org/10.5281/zenodo.15871863)
![Visitors Badge](https://visitor-badge.laobi.icu/badge?page_id=RuiGao9.GoodnessOfFitModel)<br>
# Content of this repository
This repository supports my research by providing tools to visualize model performance, particularly through numerous 1:1 scatter plots. It includes functionalities for displaying statistical summaries of those scatter plots as well as generating residual plots. The repository contains two files.<br>
- "gfit.py" contains the main function that can be called to perform analysis.<br>
- "README.md" offers a brief overview of the repository and its purpose.<br>

# Considered goodness-of-fit statistics
10 statistics are included in this function called "gfit.py". They are:<br>
- `MSE`: Mean Squared Error. Square of the unit of the output variable.<br>
- `RMSE`: Root Mean Square Error. The unit is the same as output variable.<br>
- `Bias`: Bias. The unit is the same as output variable.<br>
- `r`: correlation coefficient. Unitless.<br>
- `p-value`: p-value. Unitless.<br>
- `d`: Willmoot\'s index of agreement. Unitless.<br>
- `R2`: coefficient of determination. Unitless.<br>
- `MAE`: Mean Absolute Error. The unit is the same as output variable.<br>
- `RRMSE`: Relative Root Mean Square Error. %.<br>
- `RSD`: The standard deviation of the residual. The unit is the same as output variable.<br>

# Brief introduction of this repository
Two input vectors, observations (true) and estimations (pred), are supposed to be provided at least, and another two, “num_decimal” and “residual” are optional.<br> 
As a result, 10 statistics are returned by this python function. This output of this function can be mainly divided into 2 parts: goodness-of-fit statistics and residual plot (optional).

Any found issues are appreciated to contact Rui at Rui.Ray.Gao@gmail.com or RuiGao@UCMerced.edu.
