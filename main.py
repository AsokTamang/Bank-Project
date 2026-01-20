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
print(df_customers.annual_income)
print(df_customers[df_customers.annual_income.isnull()])
print(df_customers[df_customers.annual_income.isnull()].shape)  #total number of rows or total number of datas having null annual income


print(df_customers.isnull().sum()) #this helps us to check the null values in each column
print(df_customers.annual_income)
print(df_customers[df_customers.annual_income.isnull()])

#grouping by occupation and based on the occupation finding the annual income
occupations_median=df_customers.groupby('occupation').annual_income.median()
print(occupations_median)  #here we are calculating the median of annual income of each and every occupations

#filling the null values of a column annual income with the median of annual income based on the type of occupation.
df_customers['annual_income'] = df_customers.apply(lambda row :occupations_median[row['occupation']] if pd.isna(row['annual_income']) else row['annual_income'])



