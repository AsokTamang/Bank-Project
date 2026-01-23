import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

df=pd.read_csv("C:/Users/ashok/Downloads/chapter9_assets/chapter9_assets/8_Confidence Interval Estimate Car Miles/miles.csv")
plt.figure(figsize = (12,8))
plt.plot(df.miles)
plt.show()

n=50
sample=df.sample(n,random_state=11)  #here using random_state will always get the same sample
print(sample)


plt.figure(figsize = (12,8))
plt.plot(sample.miles)
plt.show()

sample_mean=sample.miles.mean()
sample_std = sample.miles.std()
population_std=df.miles.std()
population_mean=df.miles.mean()
print(population_mean)




z_score = norm.ppf(0.975)  #converting the probability percentage value into zscore
margin_error = z_score * (population_std/np.sqrt(n))
print(margin_error)


lower = sample_mean - margin_error
upper = sample_mean + margin_error
print(f'Confidence Interval Estimate: {lower} to {upper}')

