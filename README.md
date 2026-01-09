[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18189307.svg)](https://doi.org/10.5281/zenodo.18189307)
![Visitors Badge](https://visitor-badge.laobi.icu/badge?page_id=RuiGao9.GoodnessOfFitModel)<br>

# Content of this repository
This repository is a tool to supports my research: evaluating and visualizing model performance.

**Input:**
- At minimum, you need to provide two vectors:
  - `true`: observed (actual) values
  - `pred`: predicted values
- Optional inputs allow you to control the number of decimal places for statistics and whether to generate plots.

**Output:**
- The main function (`gfit.py`) returns a set of goodness-of-fit statistics, including MSE, RMSE, MAE, R², correlation, bias, and more.
- Optionally, you can generate plots to visualize model performance:
  - 1:1 scatter plot (predicted vs. observed)
  - Q-Q plot of residuals
  - Residual plot

The respository contains two files:
- `gfit.py`: the main analysis function
- `README.md`: this overview and usage guide

# Considered goodness-of-fit statistics
10 statistics are included in this function "gfit.py". They are:<br>
- `MSE`: Mean Squared Error. Square of the unit of the output variable.<br>
Measures the **average squared difference** between observed and predicted values. Lower values indicate better fit.
- `RMSE`: Root Mean Square Error. The unit is the same as output variable.<br>
The square root of MSE; shows the **average error** in the same units as the data.
- `Bias`: Bias. The unit is the same as output variable.<br>
The average difference between predicted and observed values. Indicates if predictions are systematically too high or too low.
- `r`: Correlation coefficient. Unitless.<br>
Measures the strength and direction of the linear relationship between observed and predicted values (ranges from -1 to 1).
- `p-value`: p-value. Unitless.<br>
  - It tells how likely it is that the result happened by random chance.
  - A **small p-value** (usually less than 0.05) means the result is probably not just random, so there is likely a real effect of relationship.
  - A **large p-value** means the result could esaily happen by chance, so there may not be a real effect.
- `d`: Willmoot\'s index of agreement. Unitless.<br>
Measures the degree of model prediction error (ranges from 0 to 1, with 1 being perfect agreement).
- `R2`: Coefficient of determination. Unitless.<br>
Shows the proportion of variance in observed values explained by the predictions (ranges from 0 to 1).
- `MAE`: Mean Absolute Error. The unit is the same as output variable.<br>
The average of the absolute differences between observed and predicted values.
- `RRMSE`: Relative Root Mean Square Error. %.<br>
RMSE expressed as a percentage of the mean observed value.
- `RSD`: The standard deviation of the residual. The unit is the same as output variable.<br>
Indicates how spread out the residuals (errors)

# Citation
If you also use this repository in your work, please cite it using the following DOI:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18189307.svg)](https://doi.org/10.5281/zenodo.18189307)

**BibTeX:**
```bibtex
@misc{gao2025goodfit,
  author       = {Rui Gao},
  title        = {Goodness of Fit Model},
  version      = v1.1.2,
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18189307},
  url          = {https://doi.org/10.5281/zenodo.18189307}
}
```

# Contact information is issues were found:
Any found issues are appreciated to contact Rui at<br> 
Rui.Ray.Gao@gmail.com <br>
RuiGao@UCMerced.edu <br>
