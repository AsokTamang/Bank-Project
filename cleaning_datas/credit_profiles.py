import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from main import df_customers,df_creditprofiles





#CREDIT PROFILES DATA
df_creditprofiles.isnull().sum()
print(df_creditprofiles.shape)
print(df_customers.shape)
print(df_creditprofiles[df_creditprofiles['cust_id'].duplicated(keep=False)])  #here we are finding if the duplicate datas exist in df_creditprofiles, keep = False means we are making the data duplicate from the very first catch


df_cp = df_creditprofiles.drop_duplicates(subset=['cust_id'], keep='last')  #as our last row has the valid data in each duplicate groups so we are dropping the first row instead
print(df_cp[df_cp.duplicated(subset=['cust_id'], keep=False)])  #checking the duplicates again

print(df_cp.isnull().sum())  #counting the number of rows having the null value
#as from the above code , we found out that the credit limit is null in the file
print(df_cp[df_cp.credit_limit.isnull()])  #here we are retrieving the data from cp where the credit limit is null

#Scatter plot of credit limit based on credit score
plt.figure(figsize=(20,8))  #here we are choosing the longer length so that the xlabel can be fitted appropriately
plt.scatter(df_cp.credit_limit,df_cp.credit_score)
plt.xlabel('Credit Limit')
plt.ylabel('Credit Score')
plt.title('Credit Limit Based on Credit Score')
plt.grid(True)
plt.xticks(range(0,90000,5000))
plt.legend()
plt.show()


#finding the null values in credit limit and filling them with the appropriate limit based on the credit_score range
bins=[299,450,500,550,600,650,700,750,800]
labels = ['300-450','451-500','501-550','551-600','601-650','651-700','701-750','751-800']
df_cp['credit_score_range'] = pd.cut(df_cp['credit_score'],bins=bins,labels=labels)
print(df_cp)
#for each range of credit_score we are assigning the highest frequently occuring credit limit
credit_score_limit= df_cp.groupby('credit_score_range')['credit_limit'].agg(lambda x:x.mode().iloc[0])  #here for each group or credit_score range we are assigning the mode value.
#and .iloc is for choosing the first value when two values are returned as a mode
print(credit_score_limit)
df_cp.isnull().sum()
# Filling NaN values in a vectorized way
df_cp['credit_limit'] = df_cp['credit_limit'].fillna(df_cp['credit_score_range'].map(credit_score_limit).astype(int))  #here as the mode value returns the float we are converting it into integer then only we are filling the null credit limit with the appropriate limit based on the credit_score range
df_cp.isnull().sum()

#cleaning the data of outstanding_debt column using clip method
(df_cp['outstanding_debt']>df_cp['credit_limit']).sum()
df_cp['outstanding_debt'] = df_cp['outstanding_debt'].clip(upper=df_cp['credit_limit'])  #clipping the outstanding debt to credit_limit as the ceiling to prevent the outstanding debt to go beyound the credit limit



#merging the credit profile data and personal info data using pandas merge function on dataframe
df_merge=df_cp.merge(df_customers,on="cust_id",how="inner")
print(df_merge)


#finding the correlation between the numerical columns
numerical_columns=['credit_limit','credit_score','credit_utilisation','age','annual_income']
correlation_matrix = df_merge[numerical_columns].corr()
plt.figure(figsize=(10, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    linecolor="white",
    square=True,
    cbar_kws={"shrink": 0.8}
)

plt.title("Correlation Matrix", fontsize=14, fontweight="bold")
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()