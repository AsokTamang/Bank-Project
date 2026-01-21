import pandas as pd
from matplotlib import pyplot as plt

df_customers = pd.read_csv("C:/Users/ashok/Downloads/chapter8_assets/chapter8_assets/dataset/customers.csv")
df_creditprofiles = pd.read_csv("C:/Users/ashok/Downloads/chapter8_assets/chapter8_assets/dataset/credit_profiles.csv")
df_transactions = pd.read_csv("C:/Users/ashok/Downloads/chapter8_assets/chapter8_assets/dataset/transactions.csv")



#CREATING A NEW COLUMN CALLED AGE-GROUP
bins = [17,25,48,65]   #here bins act as the fences between the age datas
labels = ['18-25','26-48','49-65']

df_customers['age_group']=pd.cut(
    df_customers['age'],
    bins=bins,
    labels=labels
)

data_age_group = df_customers['age_group'].value_counts(normalize=True).sort_index() * 100 #sorting the age_group and converting it into percentage
print(data_age_group)
plt.pie(data_age_group,labels = labels,autopct='%1.1f%%',shadow=True,explode=(0,0.1,0))
plt.title("Customer distribution based on age_group")
plt.show()



df_merged = df_transactions.merge(df_customers,on="cust_id",how="inner")
print(df_customers)
print(df_customers.shape)
df_customers.head(5)
df_customers.occupation.unique()
df_transactions.head(5)
df_transactions.platform.unique()










