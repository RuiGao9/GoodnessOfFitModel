[![DOI](https://zenodo.org/badge/290397319.svg)](https://doi.org/10.5281/zenodo.15871863)
![Visitors Badge](https://visitor-badge.laobi.icu/badge?page_id=RuiGao9.GoodnessOfFitModel)<br>
# Content of this repository
Three files are contained in this repository.<br>
- "Manual.pdf" explains details about this repository.<br>
- "gfit.py" is the function which can be called.<br>
- "README.md" shows a brief information about this repository.<br>

# Considered goodness-of-fit statistics
9 statistics are included in this function called "gfit.py". They are:<br>
- `RMSE`: Root Mean Square Error<br>
- `RRMSE`: Relative Root Mean Square Error<br>
- `MAE`: Mean Absolute Error<br>
- `r`: correlation coefficient<br>
- `R2`: coefficient of determination<br>
- `E`: coefficient of efficiency<br>
- `MSE`: Mean Squared Error<br>
- `RSD`: The standard deviation of the residual<br>
- `CV`: The coefficient of variation regarding the residual between the "true" and prediction values

# Brief introduction of this repository
Two input vectors, observations and estimations, are supposed to be provided at least, and another two, “type_statistic” and “residual” are optional. As a result, t score, p value, and the selected goodness-of-fit statistic are returned by this python function. This python function package mainly contains 3 parts: residual plot (optional), goodness-of-fit statistics, and the student’s t test (optional).

Details can be found in the attached manual. This repository is supposed to be modified later accordingly. If there is any mistakes, welcome leave comments and send them to me.<br>

Rui Gao<br>
rui.ray.gao@gmail.com
