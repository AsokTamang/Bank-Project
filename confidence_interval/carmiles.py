import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

df=pd.read_csv("C:/Users/ashok/Downloads/chapter9_assets/chapter9_assets/8_Confidence Interval Estimate Car Miles/miles.csv")
plt.figure(figsize = (12,8))
plt.plot(df.miles)
plt.show()

sample=df.sample(50,random_state=11)
print(sample)


plt.figure(figsize = (12,8))
plt.plot(sample.miles)
plt.show()

sample_mean=sample.miles.mean()
sample_std = sample.miles.std()
population_std=df.miles.std()
population_mean=df.miles.mean()
print(population_mean)




z_score = norm.ppf(0.975)  #converting the probability percent value into zscore
margin_error = z_score * (population_std/np.sqrt(n))
print(margin_error)


