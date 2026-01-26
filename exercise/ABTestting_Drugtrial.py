import pandas as pd
import numpy as np
from scipy.stats import norm
df_control = pd.read_csv("C:/Users/ashok/Downloads/chapter10_assets/chapter10_assets/11_z_test_AB_testing_coding/control_group.csv")
print(df_control)

df_test = pd.read_csv("C:/Users/ashok/Downloads/chapter10_assets/chapter10_assets/11_z_test_AB_testing_coding/test_group.csv")
print(df_test)

control_mean = df_control.recovery_time_hrs.mean()
control_std = df_control.recovery_time_hrs.std()
print(control_mean)
print(control_std)

test_mean = df_test.recovery_time_hrs.mean()
test_std = df_test.recovery_time_hrs.std()
print(test_std)
print(test_mean)

control_size = df_control.shape[0]  #here we are getting the shape of control group
test_size = df_test.shape[0]  #here we are getting the size of test group

a = control_std ** 2 / control_size
b = test_std ** 2 / test_size
z_score = (test_mean - control_mean) / np.sqrt(a+b)

alpha = 0.05  #the standard significant level is 0.05
z_critical = norm.ppf(1-alpha)
print(z_critical)

#as our hypothesis testing is right one-tailed test, and as our z_score is greater than z_critical ,so our z_score lies in significant or rejected region.
#so we reject the null hypothesis.


p_value = 1 - norm.cdf(z_score)
print(p_value)
#as our p_value is lesser than our alpha or significant level , we are rejecting our null hypothesis


