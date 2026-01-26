import matplotlib.pyplot as plt
import seaborn as sns

from main import df_creditprofiles,df_merged


#visual representation of percentage use of payment type across age-groups using countplot and product category count across each group
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,5))  #here we are subplotting in 1 row and 2 columns
sns.countplot(data=df_merged,x='age_group',hue='payment_type',stat="percent",ax=ax1)
ax1.set_title('Payment type Count across age-groups')
ax1.set_xlabel('age-group')
ax1.set_ylabel('payment type usage in percentage')

sns.countplot(data=df_merged,x='age_group',hue='product_category',stat="percent",ax=ax2) #so the hue is used for splitting or dividing the data with in the data, same as grouping by multiple columns
ax2.set_title('Product Category Count across age-groups')
ax2.set_xlabel('age-group')
ax2.set_ylabel('product category usage in percentage')


plt.show()


#FURTHER ANALYSIS ON AGE-GROUP
df_total_merged = df_creditprofiles.merge(df_merged,on="cust_id",how="inner")
print(df_total_merged)
operating_data = df_total_merged.groupby('age_group')[['credit_score','credit_limit','annual_income']].mean().reset_index()  #using reset_index() inorder to convert the numpy series into dataframe
print(operating_data)

columns = ['credit_score', 'credit_limit', 'annual_income']
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()
for i, col in enumerate(columns):
    sns.barplot(x='age_group', y=col, data=operating_data, ax=axes[i])
    axes[i].set_title(f'Average {col} across age-groups')
    axes[i].set_xlabel('Age-Groups')
    axes[i].set_ylabel(col)
for i in range(len(columns), len(axes)):  #removing the unused section
    fig.delaxes(axes[i])
plt.tight_layout()
plt.show()