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