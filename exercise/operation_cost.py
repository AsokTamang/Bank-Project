#You are a data scientist at a business efficiency consulting firm. Your client, a multinational corporation, has recently implemented a series of cost-saving measures across various departments. To evaluate the impact of these initiatives, the company has compiled a sample dataset named "operational_costs_data.csv". This sample dataset tracks the percentage reduction in operational costs for each department post-implementation of the cost-saving activities. The dataset includes the following columns:
#department_id: A unique identifier for each department.
#cost_reduction_pct: The percentage reduction in operational costs for each department following the cost-saving measures..
#The primary goal of the analysis is to determine whether these cost-saving measures have effectively reduced operational costs beyond the company's target of 8%.

population_mean = 7  #(indicating an average cost reduction target of 7% before the series of cost-saving measures).
population_std_dev = 3  #(variability).

import pandas as pd
import numpy as np
from scipy.stats import norm

df = pd.read_csv("C:/Users/ashok/Downloads/chapter10_exercise1/chapter10_exercise1/operational_costs_data.csv")
df.head(5)

print(df.shape)
n=100 #as there are 100 rows so the sample size is 100



#1. sample mean of cost_reduction_pct
sample_mean = df.cost_reduction_pct.mean()
print(sample_mean)

standard_error = population_std_dev / np.sqrt(n)
print(standard_error)



#defining significance level
#as our test is right tailed which states that the measures reduced cost beyound 8 %
#so the total area to the left becomes
final_probability_area =1-0.05
z_critical = norm.ppf(final_probability_area)
print(z_critical)
standard_error = population_std_dev / np.sqrt(n)
z_calculated = (sample_mean - population_mean)/ standard_error
print(z_calculated)
