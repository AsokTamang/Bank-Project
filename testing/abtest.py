import statsmodels.stats.api as sms
alpha = 0.05 #standard value
power = 0.8  #standard value
effect_sizes = [0.1, 0.2, 0.3, 0.4, 0.6, 1]
# here we are calculating the various sample sizes based on various effect sizes inorder to find the appropriate sample size for our testing
for effect_size in effect_sizes:
    sample = sms.tt_ind_solve_power(  # here we are calculating the required sample size
        effect_size=effect_size,
        alpha=alpha,
        power=power,
        ratio=1,
        alternative='two-sided')
    print(f'sample size for effect size {effect_size} is: {sample}')



