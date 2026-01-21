
import matplotlib.pyplot as plt
import seaborn as sns

from main import df_transactions


#CLEANING THE DATA OF TRANSACTIONS DATAFRAME
df_transactions.describe()
df_transactions.isnull().sum()
print(df_transactions[df_transactions['platform'].isnull()])

#determining the frequently used platform
products_based_platform = df_transactions.groupby('product_category')['platform'].agg(lambda x:x.mode().iloc[0])
print(products_based_platform)

#visual representation of frequently used platform
plt.figure(figsize=(20,8))
sns.countplot(x="product_category",hue="platform",data=df_transactions)
plt.show()

#filling the null values in the column platform using products_based_platform
df_transactions['platform'] = df_transactions['platform'].fillna(df_transactions['product_category'].map(products_based_platform))


#checking the outliers in transaction dataframe
print(df_transactions.describe())
df_zero_transaction = df_transactions[df_transactions.tran_amount==0]  #as the transaction amount cannot be 0, we must clean this tran_amount column
print(df_zero_transaction.platform)
print(df_zero_transaction.product_category)
print(df_zero_transaction.payment_type)

#finding the required replacement median value
df_new_transactions= df_transactions[(df_transactions['platform'] =="Amazon") & (df_transactions['product_category'] =="Electronics") & (df_transactions['payment_type'] =="Credit Card")]
replacing_tran_amount= df_new_transactions[df_new_transactions.tran_amount>0]['tran_amount'].median()  #as for the category, platform and payment type of the row having tran_amount 0 is same,
#we are using the median of tran amount of the row where the tran amount is greater than 0, and having that matched category, platform and payment type inorder to replace the 0 tran amount column data

print(df_transactions[df_transactions.tran_amount==0].shape)  #number of rows having transaction amount equal to 0
df_transactions.loc[df_transactions.tran_amount==0,'tran_amount'] = replacing_tran_amount  #here we are selecting the rows and columns as df_transactions.tran_amount==0,'tran_amount'  replacing it with replacing_tran_amount

print(df_transactions[df_transactions.tran_amount==0].shape)  #number of rows having transaction amount equal to 0 after cleaning the data, and the output is 0

