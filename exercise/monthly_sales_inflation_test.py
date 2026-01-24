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

