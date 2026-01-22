import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:/Users/ashok/Downloads/chapter9_assets/chapter9_assets/8_Confidence Interval Estimate Car Miles/miles.csv")
plt.figure(figsize = (12,8))
plt.plot(df.miles)
plt.show()
