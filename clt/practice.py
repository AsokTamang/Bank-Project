import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/ashok/Downloads/chapter9_assets/chapter9_assets/4_clt_solar_panels_coding/bill_survey.csv")




df['City'].nunique()  #counting the number of unique cities
df[df['City'] == 'Agra']['Bill'].mean()

#distribution of sample
sns.histplot(df[df['City'] == 'Agra'].Bill,kde=True)
plt.show()