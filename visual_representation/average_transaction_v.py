import matplotlib.pyplot as plt
import seaborn as sns

from main import df_merged


#visual representation of average transaction amount across multiple categories
col_types = ['platform','product_category','payment_type','marital_status','age_group']
fig,axes = plt.subplots(3,2,figsize=(10,12))  #here we are plotting 3 rows and 2 columns
axes = axes.flatten()  #it helps us to use the ax by index wise
for i,col in enumerate(col_types):
    avg_transaction = df_merged.groupby(col)['tran_amount'].mean().reset_index()  #with .reset_index()  we are converting the series into dataframe
    sorted_avg_transaction = avg_transaction.sort_values(by='tran_amount',ascending=False)   #we sort the values inorder for the bar chart to look better
    sns.barplot(x=col,y='tran_amount',data=sorted_avg_transaction,ax=axes[i])
    axes[i].set_title(f'Average transaction amount in {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Transaction amount')
    axes[i].set_xticklabels(axes[i].get_xticklabels(), rotation=45, ha='right') #for better readability

for i in range(len(col_types),len(axes)):
    fig.delaxes(axes[i])  #removing the unused ax
plt.tight_layout()  #for better spacing between the plots
plt.show()



