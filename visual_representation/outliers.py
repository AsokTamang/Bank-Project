import matplotlib.pyplot as plt
import seaborn as sns

from main import df_transactions



#visual representaion to check the outliers
sns.histplot(df_transactions[df_transactions.tran_amount<10000].tran_amount,bins=30)
plt.show()

#as from the figure we can see that the distribution is right-skewed
#so the best way to remove the outliers is using the quantile
q1,q3 = df_transactions.tran_amount.quantile([0.25,0.75])
iqr = q3-q1
print(iqr)
lower_limit = q1 - (2 * iqr)
upper_limit = q3 + (2 * iqr)
outliers =df_transactions[(df_transactions.tran_amount<lower_limit)|(df_transactions.tran_amount>upper_limit)]
#the below code gives us the median of tran amount for each category
tran_median_per_category= df_transactions[(df_transactions.tran_amount>lower_limit) & (df_transactions.tran_amount<upper_limit)].groupby('product_category')['tran_amount'].median()
mask = df_transactions.tran_amount>upper_limit  #as the outliers below the lower limit has been taken care of
df_transactions.loc[mask,'tran_amount'] = df_transactions.loc[mask,'product_category'].map(tran_median_per_category)

#visual representation of percentage use of payment type using countplot, where phonepe is dominant and cash is least used for transaction
sns.countplot(x=df_transactions.payment_type,stat='percent')
plt.show()


