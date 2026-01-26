#An e-commerce company is evaluating two different website designs to see which one results in higher customer engagement. Design A is the current design, while Design B incorporates new features aimed at improving user experience. The company hypothesizes that Design B will lead to a higher average time spent on the website by users.
#Datasets:
#current_design.csv: Contains data for user interactions with the current website design (Design A), with columns user_id and time_spent_minutes.
#new_design.csv: Contains data for user interactions with the new website design (Design B), with columns user_id and time_spent_minutes.
#Objective:
#To determine whether Design B results in a higher average time spent on the website compared to Design A.

import pandas as pd
import numpy as np
from scipy.stats import norm

df_current = pd.read_csv("C:/Users/ashok/Downloads/chapter10_exercise3/chapter10_exercise3/current_design.csv")
df_new = pd.read_csv("C:/Users/ashok/Downloads/chapter10_exercise3/chapter10_exercise3/new_design.csv")
print(df_current)
print(df_new)