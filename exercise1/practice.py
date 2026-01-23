import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

#You are a data scientist at a retail consulting firm. You have been provided with a dataset named "retail_store_sales_data.csv", which includes detailed records of daily sales for a retail store over a two-year period. The dataset comprises the following columns:

df = pd.read_csv("C:/Users/ashok/Downloads/chapter9_exercise/chapter9_exercise1/retail_store_sales_data.csv")
df.head(5)

#Histogram Plot of Sales Amounts
sns.histplot(df['sales_amount (usd)'])
plt.show()

#Computing Population Standard Deviation
population_std = df['sales_amount (usd)'].std()
print(population_std)

#creating a sample data and calculating its mean

n=100 #sample size
sample_data = df.sample(n,random_state = 11)
print(sample_data)
sample_mean = sample_data['sales_amount (usd)'].mean()
print(sample_mean)



#Estimating Population Mean at Various Confidence Levels

#60% Confidence Level
final_probability_60 = 0.6 + ((1-0.6) / 2)  #here as the z-scores are calculated from -inf to +z, so we must include the left tail
z_score_60 = norm.ppf(final_probability_60)
print(z_score_60)
margin_of_error_60 = z_score_60 * (population_std/np.sqrt(n))

lower_60 = sample_mean - margin_of_error_60
upper_60 = sample_mean + margin_of_error_60

print(f"60% confidence intervals - lower: {lower_60}, upper: {upper_60}")

#82% Confidence Level
final_probability_82 = 0.82 + ((1-0.82) / 2)
z_score_80 = norm.ppf(final_probability_82)
print(z_score_80)
margin_of_error_82 = z_score_80 * (population_std/np.sqrt(n))
lower_80 = sample_mean - margin_of_error_82
upper_80 = sample_mean + margin_of_error_82
print(f"80% confidence intervals - lower: {lower_80}, upper: {upper_80}")
