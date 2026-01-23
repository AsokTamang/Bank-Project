import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

#You are a data scientist at a retail consulting firm. You have been provided with a dataset named "retail_store_sales_data.csv", which includes detailed records of daily sales for a retail store over a two-year period. The dataset comprises the following columns:

df = pd.read_csv("C:/Users/ashok/Downloads/chapter9_exercise/chapter9_exercise1/retail_store_sales_data.csv")
df.head(5)
