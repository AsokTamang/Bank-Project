#An e-commerce company is evaluating two different website designs to see which one results in higher customer engagement. Design A is the current design, while Design B incorporates new features aimed at improving user experience. The company hypothesizes that Design B will lead to a higher average time spent on the website by users.
#Datasets:
#current_design.csv: Contains data for user interactions with the current website design (Design A), with columns user_id and time_spent_minutes.
#new_design.csv: Contains data for user interactions with the new website design (Design B), with columns user_id and time_spent_minutes.
#Objective:
#To determine whether Design B results in a higher average time spent on the website compared to Design A.

#null hypothesis states that the  Design B won't lead to a higher average time spent on the website by users.
#so the alternate hypothesis states that the  Design B will lead to a higher average time spent on the website by users.



import pandas as pd
import numpy as np
from scipy.stats import norm

df_current = pd.read_csv("C:/Users/ashok/Downloads/chapter10_exercise3/chapter10_exercise3/current_design.csv")
df_new = pd.read_csv("C:/Users/ashok/Downloads/chapter10_exercise3/chapter10_exercise3/new_design.csv")
print(df_current)
print(df_new)

#control statistics
current_mean = df_current.time_spent_minutes.mean()
current_std = df_current.time_spent_minutes.std()
current_size = df_current.shape[0]
print(current_mean)
print(current_std)
print(current_size)

#test statistics
test_mean = df_new.time_spent_minutes.mean()
test_std = df_new.time_spent_minutes.std()
test_size = df_new.shape[0]
print(test_mean)
print(test_std)
print(test_size)


#calculating the z_score
a=current_std**2/current_size
b= test_std ** 2 /test_size
z_score = (test_mean - current_mean) / np.sqrt(a+b)
print(z_score)

#calculating the z_critical
alpha = 0.05
z_critical = norm.ppf(1-alpha)  #as the tail is one tailed and its right tailed so we are subtracting alpha from 1 and not dividing by 2
print(z_critical)

#from the conclusion, as the z_score is larger than the z_critical, and it lies in the rejection region, so we reject the null hypothesis.
#using p_value
p_value = 1-norm.cdf(z_score)
print(p_value)
#as our p_value is also lesser than the significant level so we are rejecting null hypothesis