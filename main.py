import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
#q1a,q2a,q3a = df_customers.age.quantile([0.25,0.50,0.75])

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

#cleaning the datas


#1-filling the null values of a column annual income with the median of annual income based on the type of occupation.
df_customers['annual_income'] = df_customers.apply(lambda row :occupations_median[row['occupation']] if pd.isna(row['annual_income']) else row['annual_income'],axis=1) #here axis=1 means we are using this apply method on each rows


#ANNUAL INCOME COLUMN
#data visualization
plt.figure(figsize=(10,7))
sns.histplot(df_customers['annual_income'],kde=True,label='data')
plt.legend()
plt.show()  #right skewed histogram of annual_income data

#2-filling the outliers value with the appropriate median value
print(df_customers.annual_income.describe())
#as we can see the minimum value of annual_income is 2, which is surely a bug data
#so to clean this , we have assumed 5000 as the annual income of a person
for index,row in df_customers.iterrows():
    if row.annual_income<5000:  #if the annual income in the current row is less than 5000 then we are filling this value with the median
        df_customers.at[index,'annual_income']=occupations_median[row.occupation]
#checking the value
print(df_customers.iloc[[31]])


#AGE COLUMN
df_customers.age.isnull().sum() #checking the null values in the age column
(df_customers.age<15).sum()  #calculating the number of rows having age less than 15
(df_customers.age>80).sum()  #calculating the total number of rows having age more than 80
df_customers.age.describe()
occupation_median_age = df_customers.groupby('occupation').age.median()
df_customers['age'] = df_customers.apply(lambda row:occupation_median_age[row['occupation']] if row['age']<15 or row['age']>80 else row['age'],axis=1)   #applying this method on age column directly
print(df_customers.age.describe())
print((df_customers.age<15).sum())
sns.histplot(df_customers['age'])  #plot after removing the outliers
plt.show()

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


#CUSTOMER DISTRIBUTION BASED ON LOCATION AND GENDER
customers_location=df_customers['location'].value_counts()
print(customers_location)
#here we are using unstack inorder to convert the gender's (MALE,FEMALE) rows into column inorder for plotting
location_based_gender = df_customers.groupby('location')['gender'].value_counts().unstack()
print(location_based_gender)

location_based_gender.plot(kind='bar',stacked=True,figsize=(8,6))  #stacking the bars of male and female
plt.title("Customer Distribution based on location and gender")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()


#CREDIT PROFILES DATA
df_creditprofiles.isnull().sum()
print(df_creditprofiles.shape)
print(df_customers.shape)
print(df_creditprofiles[df_creditprofiles['cust_id'].duplicated(keep=False)])  #here we are finding if the duplicate datas exist in df_creditprofiles


df_cp = df_creditprofiles.drop_duplicates(subset=['cust_id'], keep='last')  #as our last row has the valid data in each duplicate groups so we are dropping the first row instead
print(df_cp[df_cp.duplicated(subset=['cust_id'], keep=False)])  #checking the duplicates again
