import pandas as pd

df_customers = pd.read_csv("C:/Users/ashok/Downloads/chapter8_assets/chapter8_assets/dataset/customers.csv")
df_creditprofiles = pd.read_csv("C:/Users/ashok/Downloads/chapter8_assets/chapter8_assets/dataset/credit_profiles.csv")
df_transactions = pd.read_csv("C:/Users/ashok/Downloads/chapter8_assets/chapter8_assets/dataset/transactions.csv")
print(df_customers)
print(df_customers.shape)
df_customers.head(5)
df_customers.occupation.unique()
df_transactions.head(5)
df_transactions.platform.unique()


#checking all the numeric datas
print(df_customers.describe())
q1a,q2a,q3a = df_customers.age.quantile([0.25,0.50,0.75])

#checking the null values
print(df_customers.isnull().sum()) #this helps us to check the null values in each column
