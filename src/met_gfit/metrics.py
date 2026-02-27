import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import scipy.stats as stats
from scipy.stats import pearsonr
import warnings

### === Step 1: Size Consistency Check === ###
def clean_data(true, pred):
    """
    Checking and cleaning data by removing rows with NaN or Inf values in either true or pred arrays.
    Also provides feedback to the user.
    return: (t_clean, p_clean, mask_info)
    """
    # transfer to numpy array
    true_orig = np.asarray(true)
    pred_orig = np.asarray(pred)
    
    # 1. Check size consistency
    if true_orig.shape != pred_orig.shape:
        raise ValueError(f"Size mismatch! Observed: {true_orig.shape}, Predicted: {pred_orig.shape}")

    # 2. Identifying the invalid values (NaN, +Inf, -Inf)
    # np.isfinite checking all situations at the same time
    mask = np.isfinite(true_orig) & np.isfinite(pred_orig)
    
    t_clean = true_orig[mask]
    p_clean = pred_orig[mask]
    
    # 3. Checking how many rows were removed
    n_orig = len(true_orig)
    n_clean = len(t_clean)
    n_removed = n_orig - n_clean

    # 4. Providing feedback to the user about data cleaning
    if n_removed > 0:
        # Using Warning, not print, users can choose to ignore it if they want
        msg = (
            f"\n[met-gfit Warning]: Data cleaning performed.\n"
            f"  - {n_removed} invalid rows (NaN/Inf) were detected and removed.\n"
            f"  - Valid samples for analysis: {n_clean} (out of {n_orig})."
        )
        warnings.warn(msg, UserWarning)
    
    if n_clean == 0:
        raise RuntimeError("Data Cleaning Error: No valid numeric data remains after filtering!")

    return t_clean, p_clean, {"original": n_orig, "removed": n_removed, "final": n_clean}


### === Step 2: Metrics === ###
# 1. MSE (Mean Squared Error)
def mse(true, pred):
    return np.mean((np.asarray(true) - np.asarray(pred))**2)
# 2. RMSE (Root Mean Squared Error)
def rmse(true, pred):
    return math.sqrt(mse(true, pred))
# 3. Bias (Mean Error)
def bias(true, pred):
    return np.mean(np.asarray(true) - np.asarray(pred))
# 4. Pearson's r and p-value
# Pearson r can be undefined / numerically unstable when either series is (nearly) constant
# (std close to 0 makes the correlation denominator ~0). In that case we return NaN to avoid misleading r/p-values.
def pearson_r(true, pred):
    t, p = np.asarray(true), np.asarray(pred)
    if np.std(t) < 1e-8 or np.std(p) < 1e-8:
        return np.nan, np.nan
    return pearsonr(t, p)
# 5. Pearson correlation squared
def r2_simple(true, pred):
    r, _ = pearson_r(true, pred)
    return r**2
# 6. Standard $R^2$ (Coefficient of Determination)
# R squared value (standard) in sklearn style
# Standard R2 becomes undefined / unstable when the target variance is (near) zero (SS_tot close to 0).
# We guard against this and return NaN instead of reporting a meaningless $R^2$.
def r2_standard(true, pred):
    t, p = np.asarray(true), np.asarray(pred)
    ss_res = np.sum((t - p) ** 2)
    ss_tot = np.sum((t - np.mean(t)) ** 2)
    return 1 - (ss_res / ss_tot) if ss_tot > 1e-8 else np.nan
# 7. MAE (Mean Absolute Error)
def mae(true, pred):
    return np.mean(np.abs(np.asarray(true) - np.asarray(pred)))
# 8. RRMSE (Relative Root Mean Squared Error)
def rrmse(true, pred):
    t = np.asarray(true)
    m = np.mean(t)
    return (rmse(t, pred) / m * 100) if m != 0 else np.nan
# 9. Willmott's d index
def d_index(true, pred):
    t, p = np.asarray(true), np.asarray(pred)
    mean_t = np.mean(t)
    num = np.sum((t - p)**2)
    den = np.sum((np.abs(p - mean_t) + np.abs(t - mean_t))**2)
    return 1 - (num / den) if den != 0 else np.nan
# 10. RSD (Residual Standard Deviation)
def rsd(true, pred):
    return np.std(np.asarray(true) - np.asarray(pred))


### === Step 3: Plots === ###
def plot_diagnostics(true, pred):
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Garamond", "Adobe Garamond Pro", "Eb Garamond", "Times New Roman"],
        "font.size": 12,
        "axes.titlesize": 12,
        "axes.labelsize": 12, 
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.titlesize": 14
    })

    """Plot 1:1, scatters, Q-Q, and residual plots"""
    true = np.asarray(true)
    pred = np.asarray(pred)
    diff = true - pred
    
    fig = plt.figure(figsize=(10, 8))
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 0.7])

    # 1:1 scatter plot
    ax1 = fig.add_subplot(gs[0, 0])
    max_val = max(np.max(true), np.max(pred))
    min_val = min(np.min(true), np.min(pred))
    ax1.scatter(pred, true, color='blue', alpha=0.6, label='Pred vs Obs')
    ax1.plot([min_val, max_val], [min_val, max_val], 'r--', label='1:1 Line')
    ax1.set_xlabel('Predictions')
    ax1.set_ylabel('Observations')
    ax1.set_title('Scatter Plot with 1:1 Line')
    ax1.legend()
    ax1.set_aspect('equal', adjustable='box')

    # Q-Q plot of residuals
    ax2 = fig.add_subplot(gs[0, 1])
    stats.probplot(diff, dist="norm", plot=ax2)
    ax2.set_title("Q-Q Plot of Residuals")

    # Residual plot
    ax3 = fig.add_subplot(gs[1, :])
    ax3.scatter(range(len(diff)), diff, alpha=0.6)
    ax3.axhline(y=0, color='r', linestyle='--')
    ax3.set_ylabel("Residual")
    ax3.set_xlabel("Index")
    ax3.set_title("Residual Plot")

    plt.tight_layout()
    plt.show()


### === Step 4: Combine them together === ###
def gfit(true, pred, num_decimal=3, plots='Yes', show_results='Yes'):
    # Transfer to Numpy for easily processing
    t_arr = np.asarray(true)
    p_arr = np.asarray(pred)
    
    # --- 1. Cleaning warnings ---
    original_n = len(t_arr)
    
    # Checking items including, NaN and Inf)
    mask = np.isfinite(t_arr) & np.isfinite(p_arr)
    t_clean = t_arr[mask]
    p_clean = p_arr[mask]
    
    n_val = len(t_clean)
    removed_n = original_n - n_val

    # Warning to user if any invalid points were removed
    if removed_n > 0:
        warning_msg = (
            f"\n[met-gfit Warning]: {removed_n} invalid points (NaN/Inf) were detected and removed. "
            f"Analysis proceeding with n = {n_val} (Original n = {original_n})."
        )
        warnings.warn(warning_msg, UserWarning)

    # Regular checks after cleaning
    if n_val == 0:
        print("Error: No valid data points left after cleaning!")
        return None

    if t_clean.shape != p_clean.shape:
        print("Error: Size mismatch between observed and predicted vectors!")
        return None

    # --- 2. Calculate those values ---
    mse_val = mse(t_clean, p_clean)
    rmse_val = rmse(t_clean, p_clean)
    bias_val = bias(t_clean, p_clean)
    r_val, p_val = pearson_r(t_clean, p_clean)
    r2_s = r2_simple(t_clean, p_clean)
    r2_std = r2_standard(t_clean, p_clean)
    mae_val = mae(t_clean, p_clean)
    rrmse_val = rrmse(t_clean, p_clean)
    rsd_val = rsd(t_clean, p_clean)
    d_val = d_index(t_clean, p_clean)

    # --- 3. Plots? ---
    if plots == 'Yes':
        plot_diagnostics(t_clean, p_clean)

    # --- 4. Print results ---
    if show_results == 'Yes':
        fmt = f".{num_decimal}f"
        print(f"\n" + "="*40)
        print(f"      MODEL EVALUATION REPORT")
        print("="*40)
        if removed_n > 0:
            print(f"Data Cleaning: {removed_n} rows removed (NaN/Inf)")
        print(f"Number of cases (n): {n_val}")
        print("-" * 40)
        print(f"MSE:            {mse_val:{fmt}}")
        print(f"RMSE:           {rmse_val:{fmt}}")
        print(f"RRMSE:          {rrmse_val:{fmt}}")
        print(f"Bias:           {bias_val:{fmt}}")
        print(f"MAE:            {mae_val:{fmt}}")
        print(f"Standard R2:    {r2_std:{fmt}}")
        print(f"Simple R2:      {r2_s:{fmt}}")
        print(f"Pearson r:      {r_val:{fmt}} (p={p_val:.2e})")
        print(f"Willmott's d:   {d_val:{fmt}}")
        print(f"RSD:            {rsd_val:{fmt}}")
        print("="*40 + "\n")

    return (n_val, mse_val, rmse_val, bias_val, r_val, p_val, r2_s, r2_std, d_val, mae_val, rrmse_val, rsd_val)