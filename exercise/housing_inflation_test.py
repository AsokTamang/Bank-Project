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


