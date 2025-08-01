def gfit(true, pred, num_decimal=3, residual='Yes'):
    """
    Calculates goodness-of-fit statistics and optionally plots residuals.

    Parameters:
    true (array-like): Observed values.
    pred (array-like): Predicted values.
    num_decimal (int): Number of decimals for printed output.
    residual (str): If 'Yes', show residual plot.
    type_statistic (str or None): If set, returns only the specified statistic:
        '1': RMSE
        '2': RRMSE
        '3': MAE
        '4': r (Pearson correlation)
        '5': R2
        '6': E (coefficient of efficiency)
        '7': MSE
        '8': RSD (std of residual)
        '9': CV (coefficient of variation of residual)
        Otherwise, prints and returns all statistics.

    Returns:
    Returns a tuple: (n, mse, rmse, bias, r, p_value, d, r2, mae, rrmse, rsd)
    """
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    import statistics
    from scipy.stats import pearsonr

    true = np.asarray(true)
    pred = np.asarray(pred)

    if true.shape != pred.shape:
        print("\nError! The size of vector 1 does not match vector 2!\n")
        return None

    diff = true - pred
    mean_true = true.mean()

    # Residual plot
    if residual == 'Yes':
        plt.figure(figsize=(5, 2.5))
        plt.scatter(range(1, 1 + len(true)), diff)
        plt.plot(range(1, 1 + len(true)), [0] * len(true), 'r--')
        plt.xlim(0, len(true) + 1)
        plt.ylabel("Residual")
        plt.show()

    # Statistics
    n = len(true)
    mse = np.mean(diff ** 2)
    rmse = math.sqrt(mse)
    bias = np.mean(diff)
    r, p_value = pearsonr(true, pred)
    r2 = r ** 2
    mae = np.mean(np.abs(diff))
    rrmse = rmse / mean_true * 100 if mean_true != 0 else np.nan
    rsd = np.std(diff)
    # Willmott's index of agreement
    tmp_1 = np.sum((true - pred) ** 2)
    tmp_2 = np.mean(true)
    tmp_3 = np.sum((np.abs(true - tmp_2) + np.abs(pred - tmp_2)) ** 2)
    d = 1 - (tmp_1 / tmp_3) if tmp_3 != 0 else np.nan

    fmt = f".{num_decimal}f"
    # Print all statistics
    print(f'Number of cases: {n:.0f}')
    print(f'Mean square error (MSE): {mse:{fmt}}')
    print(f'Root mean square error (RMSE): {rmse:{fmt}}')
    print(f'Relative RMSE (RRMSE): {rrmse:{fmt}}')
    print(f'Mean absolute error (MAE): {mae:{fmt}}')
    print(f'Bias: {bias:{fmt}}')
    print(f'Pearson correlation (r): {r:{fmt}}')
    print(f'R squared (R2): {r2:{fmt}}')
    print(f'P-value: {p_value:.2e}')
    print(f'Willmott\'s index of agreement (d): {d:{fmt}}')
    print(f'Standard deviation of residual (RSD): {rsd:{fmt}}')

    return (n, mse, rmse, bias, r, p_value, d, r2, mae, rrmse, rsd)