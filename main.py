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
