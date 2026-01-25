import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import numpy as np

df = pd.read_csv("C:/Users/ashok/Downloads/chapter10_assets/chapter10_assets/3_z_test_housing_inflation/house_price_increase.csv")

population_mean = df.price_increase_pct.mean()
population_std = df.price_increase_pct.std()
print(population_mean)


#calculating the sample
n = 50
df_sample = df.sample(50,random_state = 11)
print(df_sample)

sample_mean = df_sample.price_increase_pct.mean()
print(sample_mean)

standard_error = population_std / (np.sqrt(n))
print(standard_error)

#calculating the zscore
z_score = (sample_mean - population_mean) / standard_error
print(z_score)

alpha = 0.05
confidence_level = 1 - alpha

z_critical = norm.ppf(confidence_level)
print(z_critical)



#now we compare our calculated z_score with the z_critical
# in the case of right tailed  which is one_tailed testing if the z_score is greater than z_critical then we reject the null hypothesis as z_score lies within the significant region
# in the case of left tailed  which is one_tailed testing if the z_score is lesser than z_critical then we reject the null hypothesis as z_score lies within the significant region
# in the case of two_tailed testing , if the z_score is either lesser than negative z_critical or greater than positive z_critical then we reject the null hypothesis.


#in one_tailed test , the alpha or significant level is used in one of the tail only
#in two_tailed test , the alpha or significant level is divided equally on both sides

#the standard sample size for testing is either 30 or greater than 30


area_to_left = norm.cdf(z_score)  #this gets us the area to the left under the curve using calculated z score
#as our current test is one tailed
p_value = 1 - area_to_left  #if our test was two tailed then we would multiply this current value
print(p_value)

#if the p_value is lesser than significant level or alpha then we reject the null hypothesis
#otherwise we would accept the null hypothesis


#if the alternate hypothesis states that the inflation of housing price is not equal to 10%, then the test becomes two tailed test,
#then we must divide the significant level into half inorder to calculate the z_critical based on area to the left
z_critical1 = norm.ppf(1-(alpha/2))
print(z_critical1)
#as the z_score is lesser than z_critical , then we cannot reject the null hypothesis

#and for the case of p_value
p_value1 =  2 *(1 - area_to_left)  #if our test was two tailed then we would multiply this current value
print(p_value1)
print(alpha)

#since p_value1 is greater than the significant level, then the null hypothesis is accepted




