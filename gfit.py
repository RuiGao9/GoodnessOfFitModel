def gfit(true, pred, num_decimal=3, plots='Yes'):
    """
    Calculates goodness-of-fit statistics and optionally plots residuals.

    Parameters:
    true (array-like): Observed values.
    pred (array-like): Predicted values.
    num_decimal (int): Number of decimals for printed output.
    plots (str): If 'Yes', show residual plot and Q-Q plot.
    type_statistic (str or None): If set, returns only the specified statistic:
        
    Returns:
    Returns a tuple: (n, mse, rmse, bias, r, p_value, r2_simple, r2_standard, d, mae, rrmse, rsd)
        1. The number of cases (n)
        2. Mean Square Error (MSE)
        3. Root Mean Square Error (RMSE)
        4. Bias
        5. Pearson correlation coefficient (r)
        6. p-value of the correlation
        7. r-squared (Pearson^2)
        8. Standard R-squared (R2)
        9. Willmott's index of agreement (d)
        10. Mean Absolute Error (MAE)
        11. Relative RMSE (RRMSE)
        12. Standard Deviation of Residuals (RSD)
    """
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    import scipy.stats as stats
    from scipy.stats import pearsonr

    true = np.asarray(true)
    pred = np.asarray(pred)
    
    # Take off rows containing NaN
    mask = np.isfinite(true) & np.isfinite(pred)
    true = true[mask]
    pred = pred[mask]

    if true.shape != pred.shape:
        print("\nError! The size of vector 1 does not match vector 2!\n")
        return None

    diff = true - pred
    mean_true = true.mean()

    # Plots or not
    if plots == 'Yes':
        import matplotlib.gridspec as gridspec

        fig = plt.figure(figsize=(10, 6))
        gs = gridspec.GridSpec(2, 2, height_ratios=[1, 0.7])

        # 1:1 scatter plot (top left)
        ax1 = fig.add_subplot(gs[0, 0])
        max_value = np.max([np.max(true), np.max(pred)])
        min_value = np.min([np.min(true), np.min(pred)])
        ax1.scatter(pred, true, color='blue', label='Pred vs Observ')
        ax1.plot([min_value, max_value], [min_value, max_value], 'r--', label='1:1 Line')
        ax1.set_xlim(min_value, max_value)
        ax1.set_ylim(min_value, max_value)
        ax1.set_xlabel('Predictions')
        ax1.set_ylabel('Observations')
        ax1.set_title('Scatter Plot with 1:1 Line')
        ax1.legend()
        ax1.grid(False)
        ax1.set_aspect('equal', adjustable='box')

        # Q-Q plot (top right)
        ax2 = fig.add_subplot(gs[0, 1])
        stats.probplot(diff, dist="norm", plot=ax2)
        ax2.set_title("Q-Q Plot of Residuals")

        # Residual plot (bottom, spanning both columns)
        ax3 = fig.add_subplot(gs[1, :])
        ax3.scatter(range(1, 1 + len(true)), diff)
        ax3.plot(range(1, 1 + len(true)), [0] * len(true), 'r--')
        ax3.set_xlim(0, len(true) + 1)
        ax3.set_ylabel("Residual")
        ax3.set_xlabel("Index")
        ax3.set_title("Residual Plot")

        plt.tight_layout()
        plt.show()

    # Statistics
    n = len(true)
    mse = np.mean(diff ** 2)
    rmse = math.sqrt(mse)
    bias = np.mean(diff)

    r, p_value = pearsonr(true, pred)
    
    # Pearson correlation squared
    r2_simple = r ** 2
    # R squared value (standard) in sklearn style
    ss_res = np.sum((true - pred) ** 2)
    ss_tot = np.sum((true - mean_true) ** 2)
    r2_standard = 1- (ss_res / ss_tot)

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
    print(f'r-squared, Pearson^2 (r2): {r2_simple:{fmt}}')
    print(f'Standard (R2): {r2_standard:{fmt}}')
    print(f'p-value: {p_value:.2e}')
    print(f'Willmott\'s index of agreement (d): {d:{fmt}}')
    print(f'Standard deviation of residual (RSD): {rsd:{fmt}}')

    return (n, mse, rmse, bias, r, p_value, r2_simple, r2_standard, d, mae, rrmse, rsd)