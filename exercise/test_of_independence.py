
import numpy as np
import sys
from scipy.stats import chi2,chi2_contingency

observed = np.array([[0,60],
                     [70,40]])
alpha = 0.05
r = len(observed)
c=len(observed[0])
degree_of_freedom = (r-1) * (c-1)
print(degree_of_freedom)

critical_value = chi2.ppf(1-alpha,degree_of_freedom)
print(critical_value)


chi_squared,p_value , dof,freq = chi2_contingency(observed)  #this helps us to build the expected value and calculate the chi_squared value
alpha = 0.05
print(chi_squared)

#as the chi_squared value is greater than the critical value so the this value lies in the rejection region, hence we are rejecting the null hypothesis which has stated that there is no relation between two variables


