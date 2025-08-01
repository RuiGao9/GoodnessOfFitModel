% filepath: c:\GitHub\GoodnessOfFitModel\matlab_gfit.m
function result = matlab_gfit(true, pred)
    % Calculates goodness-of-fit statistics between true and predicted values.
    % Output order matches Python gfit: [n, mse, rmse, bias, r, p_value, d, r2, e, mae, rrmse, rsd, cv]

    diff = true - pred;
    n = length(true); % Number of cases
    mse = mean(diff.^2); % Mean squared error
    rmse = sqrt(mse); % Root mean squared error
    bias = mean(diff); % Mean bias (true - pred)
    [r, p_value] = corr(true, pred); % Pearson correlation and p-value
    r2 = r^2; % R squared
    mae = mean(abs(diff)); % Mean absolute error
    rrmse = rmse / mean(true) * 100; % Relative RMSE (%)
    rsd = std(diff); % Standard deviation of residuals
    mean_diff = mean(diff);
    if mean_diff ~= 0
        cv = rsd / mean_diff * 100; % Coefficient of variation of residuals (%)
    else
        cv = NaN;
    end
    tmp_1 = sum((true - pred).^2);
    tmp_2 = mean(true);
    tmp_3 = sum((abs(true - tmp_2) + abs(pred - tmp_2)).^2);
    if tmp_3 ~= 0
        d = 1 - (tmp_1 / tmp_3); % Willmott's index of agreement
    else
        d = NaN;
    end
    if sum((true - mean(true)).^2) ~= 0
        e = 1 - sum((diff).^2) / sum((true - mean(true)).^2); % Coefficient of efficiency
    else
        e = NaN;
    end
    result = [n, mse, rmse, bias, r, p_value, d, r2, e, mae, rrmse, rsd, cv];
end

