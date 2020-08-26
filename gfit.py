def gfit(true,pred,type_statistic='9'):
  import numpy as np
  # Size of two vectors should be the same
  if true.shape == pred.shape:
    pass
  else:
    print("Error! The size of vector 1 does not match vector 2!")
  # Basic information about inputs
  num_element = len(true)
  diff = true - pred
  mean_true = true.mean()
  mean_pred = pred.mean()
  # Calculate the statistics
  if type_statistic == '1': # mean squarred error
    out = (diff**2).mean()
    # https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=4775883
  elif type_statistic == '2': # normalized mean squarred error
    out = (diff**2).mean()/(np.var(true))
  elif type_statistic == '3': # root mean squarred error
    out = np.sqrt((diff**2).mean())
    # https://www.researchgate.net/profile/Tianfeng_Chai/publication/272024186_Root_mean_square_error_RMSE_or_mean_absolute_error_MAE-_Arguments_against_avoiding_RMSE_in_the_literature/links/54e3776f0cf2b2314f5d2f3c/Root-mean-square-error-RMSE-or-mean-absolute-error-MAE-Arguments-against-avoiding-RMSE-in-the-literature.pdf
  elif type_statistic == '4': # normalized root mean squarred error
    out = np.sqrt((diff**2).mean()/(np.var(true)))
  elif type_statistic == '5': # mean absolute error
    out = (abs(diff)).mean()
    # https://www.researchgate.net/profile/Tianfeng_Chai/publication/272024186_Root_mean_square_error_RMSE_or_mean_absolute_error_MAE-_Arguments_against_avoiding_RMSE_in_the_literature/links/54e3776f0cf2b2314f5d2f3c/Root-mean-square-error-RMSE-or-mean-absolute-error-MAE-Arguments-against-avoiding-RMSE-in-the-literature.pdf
  elif type_statistic == '6': # mean absolute relative error
    out = (abs(np.divide(diff,true))).mean()
  elif type_statistic == '7': # coefficient of correlation
    out = np.corrcoef(true,pred)
    out = out[0,1]
  elif type_statistic == '8': # coefficient of determination
    tmp = np.corrcoef(true,pred)
    tmp = tmp[0,1]
    out = tmp**2
    # Incorporation of Unmanned Aerial Vehicle (UAV) Point Cloud Products into Remote Sensing Evapotranspiration Models
    # https://reader.elsevier.com/reader/sd/pii/S0196890413001118?token=3EF9DF2D9665F935B37C107225B96F719ECDA28AF240B1B0F5350FFE8171D504D46207A6C3C213037CF82A7CC90D5A83
    # https://stats.stackexchange.com/questions/185898/difference-between-nash-sutcliffe-efficiency-and-coefficient-of-determination?newreg=bbdb5cc0c3db4071a7beb9b3e523acb0
  elif type_statistic == '9': # coefficient of efficiency
    out = 1 - (diff**2).sum()/((true - mean_true)**2).sum()
  elif type_statistic == '10':  # relative root mean square error
    out = np.sqrt((diff**2).mean())
    out = out/mean_true*100
  return(out)  