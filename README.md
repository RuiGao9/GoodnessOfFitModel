[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18807443.svg)](https://doi.org/10.5281/zenodo.18807443)
![Visitors Badge](https://visitor-badge.laobi.icu/badge?page_id=RuiGao9/met_gfit)<br>

# Model Evaluation Toolkit
A streamlined Python toolkit for comprehensive model evaluation. met-gfit automates the calculation of 10 key statistical metrics and generates professional diagnostic plots (1:1 scatter, Residual, and Q-Q plots) to validate and visualize model accuracy with ease.

## Input
- At minimum, you need to provide two vectors:
  - `true`: observed (actual) values
  - `pred`: predicted values
- Optional inputs allow you to control the number of decimal places for statistics and whether to generate plots.

## Comprehensive Evaluation
The core function `gfit()` performs a full-scale diagnostic of your model, providing:
- **12 Statistical Metrics**: Returns a dictionary/report containing $R^2$, $RMSE$, $MAE$, $Bias$, $r$, $d$-index, and more.
- **Visual Diagnostics**: Optionally generates a professional three-panel figure including:
  - **1:1 Scatter Plot**: Visualizes accuracy and potential scaling issues.
  - **Residual Plot**: Checks for non-linearity and heteroscedasticity.
  - Q-Q Plot: Evaluates the normality of the error distribution.
## File Structure
The repository is organized following the standard Python `src` layout for better compatibility and installation:
- `src/met_gfit/`:
  - `metrics.py`: The engine containing all mathematical formulas and plotting logic.
  - `__init__.py`: The gateway that allows for clean imports (e.g., `from met_gfit import gfit`).
- pyproject.toml: Project metadata and dependency specifications.
- README.md: This comprehensive documentation and user guide.
- LICENSE: MIT License for open-source use.

# Considered goodness-of-fit statistics
10 statistics are included in this function "gfit.py". They are:<br>
- `MSE`: Mean Squared Error. Square of the unit of the output variable.<br>
Measures the **average squared difference** between observed and predicted values. Lower values indicate a better fit.
- `RMSE`: Root Mean Square Error. The unit is the same as output variable.<br>
The square root of MSE; shows the **average error** in the same units as the data.
- `Bias`: Bias. The unit is the same as output variable.<br>
The average difference between predicted and observed values. Indicates if predictions are systematically too high or too low.
- `r`: Correlation coefficient. Unitless.<br>
Measures the strength and direction of the linear relationship between observed and predicted values (ranges from -1 to 1).
- `p-value`: p-value. Unitless.<br>
  - It tells how likely it is that the result happened by random chance.
  - A **small p-value** (usually less than 0.05) means the result is probably not just random, so there is likely a real effect of the relationship.
  - A **large p-value** means the result could easily happen by chance, so there may not be a real effect.
- `d`: Willmoot\'s index of agreement. Unitless.<br>
Measures the degree of model prediction error (ranges from 0 to 1, with 1 being perfect agreement).
- `R2`: Coefficient of determination. Unitless.<br>
Shows the proportion of variance in observed values explained by the predictions (ranges from 0 to 1).
- `MAE`: Mean Absolute Error. The unit is the same as the output variable.<br>
The average of the absolute differences between observed and predicted values.
- `RRMSE`: Relative Root Mean Square Error. %.<br>
RMSE expressed as a percentage of the mean observed value.
- `RSD`: The standard deviation of the residual. The unit is the same as the output variable.<br>
Indicates how spread out the residuals (errors)

# Equations
**met_gfit** provides a comprehensive assessment of model performance, covering accuracy, precision, and agreement with observations. The following statistics are implemented:
### Mean Square Error ($MSE$)
Measures the average of the squares of the errors, giving more weight to larger deviations (outliers).<br>
$$MSE=\frac{1}{n}\sum_{i=1}^{n}(o_i-p_i)^2$$

### Root Mean Square Error ($RMSE$)
Indicates how much the model’s predictions deviate from the observations on average.<br>
$$RMSE=\sqrt{\frac{\sum_{i=1}^{n}(o_i-\hat{p}_i)^2}{n}}$$

### Mean Bias ($Bias$)
Measures the average tendency of the model to over- or under-estimate the observed values. A positive value indicates overestimation.<br>
$$Bias=\frac{1}{n}\sum_{i=1}^{n}(p_i-o_i)$$

### Pearson Correlation Coefficient ($r$)
Indicates the strength and direction of the linear relationship between predicted and observed values. A correlation close to 1 or -1 indicates that the model captures the variability of observations well.<br>
$$r=\frac{cov{(o,p)}}{\sigma_o\sigma_p} $$

### Willmott's Index of Agreement ($d$)
Considers both the mean absolute error and the variability of the observations, showing insight into how well the model replicates the variability and pattern of the observations (Willmott, 1982).<br>
$$d=1-\frac{\sum_{i=1}^{n}(o_i-p_i)^2}{\sum_{i=1}^{n}(|p_i-\bar{o}|+|o_i-\bar{o}|)^2}$$

### Coefficient of Determination ($R^2$)
Quantifies the proportion of the variance in the observations that is predictable from the model, providing a rigorous measure of model fit.<br>
$$R^2=1- \frac{\sum_{i=1}^{n}(o_i-\hat{p}_i)^2}{\sum_{i=1}^{n}(o_i-\bar{o})^2}$$

### Mean Absolute Error ($MAE$)
Represents the average of the absolute differences between observations and predictions, providing a linear score where all individual differences are weighted equally.<br>
$$MAE=\frac{1}{n}\sum_{i=1}^{n}|o_i-p_i|$$

### Relative Root Mean Square Error ($RRMSE$)
Normalizes the $RMSE$ by the mean of the observations, expressed as a percentage, which allows for comparison between different datasets or variables.<br>
$$RRMSE=\frac{RMSE}{\bar{o}}\times100\%$$

### Residual Standard Deviation ($RSD$)
Quantifies the spread of the residuals (the differences between model and observations) around their mean.<br>
$$RSD=\sqrt{\frac{\sum_{i=1}^{n}(p_i-o_i-\frac{1}{n}\sum_{i=1}^{n}(p_i-o_i))^2}{n-1}}$$

where $o$ represents observations, $o_i$ is the observed value for the ith observations, $\bar{o}$ is the mean of observations, $p$ represents predictions, $p_i$ is the estimated value for the ith estimations, $\hat{p}_i$ is the estimated value corresponding to the ith observations, $n$ is the number of paired observations.

# Reference
- Willmott, C. J. (1982). Some comments on the evaluation of model performance. Bulletin of the American Meteorological Society, 63(11), 1309-1313. https://doi.org/10.1175/1520-0477(1982)063<1309:SCOTEO>2.0.CO;2
- Nash, J. E., & Sutcliffe, J. V. (1970). River flow forecasting through conceptual models part I — A discussion of principles. Journal of Hydrology, 10(3), 282-290. (For $NSE$/$R^2$ implementation).

# Software Citation
If you also use this repository in your work, please cite it using the following DOI:<br>
**Gao, R. (2025).** *met_gfit: A Python toolkit for comprehensive model evaluation and diagnostic plotting.* Version 1.1.3. Zenodo: https://doi.org/10.5281/zenodo.18807443

<summary><b>Click to copy BibTeX for citation</b></summary>

```bibtex
@misc{gao2025met_gfit,
  author       = {Rui Gao},
  title        = {met_gfit: A Python toolkit for comprehensive model evaluation and diagnostic plotting},
  version      = v1.1.3,
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18189307},
  url          = {[https://doi.org/10.5281/zenodo.18807443](https://doi.org/10.5281/zenodo.18807443)}
}
```

# Contact information if issues were found:
Any found issues are appreciated to contact Rui at<br> 
Rui.Ray.Gao@gmail.com <br>
RuiGao@UCMerced.edu <br>
