import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/ashok/Downloads/chapter9_assets/chapter9_assets/4_clt_solar_panels_coding/bill_survey.csv")




df['City'].nunique()  #counting the number of unique cities
df[df['City'] == 'Agra']['Bill'].mean()

#distribution of sample
sns.histplot(df[df['City'] == 'Agra'].Bill,kde=True)
plt.show()


sample_mean = df.groupby('City')['Bill'].mean()
print(sample_mean)

sns.histplot(sample_mean,kde=True)  #so the distribution of all the samples or the sampling distribution is approx. normal distrubution
#which means that the mean of this sampling distribution is nearly equal to the mean of entire population
plt.show()
