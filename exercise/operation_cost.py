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