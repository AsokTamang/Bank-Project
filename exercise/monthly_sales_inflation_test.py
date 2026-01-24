import pandas as pd
import sys
import numpy as np
sys.path.append(r"C:\pythonprojects\bank_project\venv\Lib\site-packages")
from scipy.stats import norm


#given population parameters

population_mean = 12  #(This implies that before the new campaign, the average increase in sales was around 12%)
population_std_dev = 5  #(variability)

df = pd.read_csv("C:/Users/ashok/Downloads/chapter10_exercise2/chapter10_exercise2/monthly_sales_data.csv")
print(df)

#so here the null hypothesis states that the campaign hasnot increased the average monthly sales more than 15%
#and the alternate hypothesis states that the campaign has increased the average monthly sales more than 15 %
#so the testing is right one tailed test

#1. sample mean of cost_reduction_pct
n = df.shape[0]
print('sample size is:', n)
sample_mean = df.sales_increase_pct.mean()
standard_error = population_std_dev / np.sqrt(n)
print(standard_error)

#2. sample size

z_score = (sample_mean - population_mean) / standard_error
print(z_score)

#defining significance level
area_to_left = norm.cdf(z_score)
p_value = 1 - area_to_left  #as the tail is one right tailed we are subtracting from 1 and not multiplying by 2

#decision_making
#as the p_value is very small than the significant level so we reject the null hypothesis that states that the  campaign hasn't increased the average monthly sales more than 15%