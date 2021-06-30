# Content of this repository
Three files are contained in this repository.<br>
- "Manual.pdf" explains details about this repository.<br>
- "gfit.py" is the function which can be called.<br>
- "README.md" shows a brief information about this repository.<br>

# Considered goodness-of-fit statistics
8 statistics are included in this function called "gfit.py". They are:<br>
- `RMSE`: Root Mean Square Error<br>
- `RRMSE`: Relative Root Mean Square Error<br>
- `MAE`: Mean Absolute Error<br>
- `r`: correlation coefficient<br>
- `R2`: coefficient of determination<br>
- `E`: coefficient of efficiency<br>
- `MSE`: Mean Squared Error<br>
- `RSD`: The standard deviation of the residual

# Brief introduction of this repository
Two input vectors, observations and estimations, are supposed to be provided at least, and another two, “type_statistic” and “residual” are optional. As a result, t score, p value, and the selected goodness-of-fit statistic are returned by this python function. This python function package mainly contains 3 parts: residual plot (optional), goodness-of-fit statistics, and the student’s t test (optional).

Details can be found in the attached manual. This repository is supposed to be modified later accordingly. If there is any mistakes, welcome leave comments and send them to me.<br>

Rui Gao<br>
rui.gao@aggiemail.usu.edu
