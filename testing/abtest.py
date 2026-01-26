import statsmodels.stats.api as sms
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import norm
alpha = 0.05 #standard value
power = 0.8  #standard value
effect_sizes = [0.1, 0.2, 0.3, 0.4, 0.6, 1]
# here we are calculating the various sample sizes based on various effect sizes inorder to find the appropriate sample size for our testing
for effect_size in effect_sizes:
    sample = sms.tt_ind_solve_power(  # here we are calculating the required sample size for testing the usage of new credit card
        effect_size=effect_size,
        alpha=alpha,
        power=power,
        ratio=1,
        alternative='two-sided')
    print(f'sample size for effect size {effect_size} is: {sample}')

#after choosing the appropriate sample size, we select that size of customers to use the new credit card, then from this population,
#then we will get a certain size of population who uses this new credit card
#so we use this same number of people or same sample size as our control group size to use the old credit card, excluding the people who were given to use the new credit card


df = pd.read_csv("C:/Users/ashok/Downloads/chapter11_assets/chapter11_assets/data/avg_transactions_after_campaign.csv")
print(df)


fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,6))
sns.histplot(df.control_group_avg_tran,kde=True,label='Control group average transaction',ax=ax1)
ax1.set_xlabel('Sales')
ax1.set_ylabel('Frequency')
ax1.set_title('Distribution of average control group transaction')
ax1.legend()

sns.histplot(df.test_group_avg_tran,kde=True,color='g',label='Test group average transaction',ax=ax2)
ax2.set_xlabel('Sales')
ax2.set_ylabel('Frequency')
ax2.set_title('Distribution of average Test group transaction')
ax2.legend()

plt.show()


n = df.shape[0]  #sample size
print(f'The sample size is:', n)
#and as our sample size is greater than 30 we are using z_test in our AB testing

#statistics for control group
control_mean = df.control_group_avg_tran.mean()
control_std = df.control_group_avg_tran.std()
print(control_mean)
print(control_std)

#statistics for test group
test_mean = df.test_group_avg_tran.mean()
test_std = df.test_group_avg_tran.std()
print(test_mean)
print(test_std)

a = (test_std ** 2 / n)
b =   (control_std ** 2 / n)
z_score = (test_mean - control_mean) / np.sqrt(a+b)
print(z_score)

z_critical = norm.ppf(1-alpha)
print(z_critical)


#as we can observe, the z_score is greater than the z_critical. so the z_score of sample lies in the rejection region
#which concludes that the null hypothesis (the new credit card avg transaction is not better than that of old credit card) is rejected.

p_value = 1-norm.cdf(z_score)
print(p_value)
#as p_value is also lesser than the significant level
#so the null hypothesis is rejected
#we are good to launch our new credit card


#calculating the interval where the amount of average transaction using new credit card lies
confidence_interval = 1- alpha
print(confidence_interval)
average_tran_new = norm.interval(confidence_interval,loc=test_mean,scale=test_std/np.sqrt(n))
print(average_tran_new)