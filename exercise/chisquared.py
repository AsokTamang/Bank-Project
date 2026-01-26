### import pandas as pd
import numpy as np
import sys
sys.path.append(r"C:\pythonprojects\bank_project\venv\Lib\site-packages")
import scipy.stats as st
alpha = 0.05
expected = np.array([40,30,60,70])  #the sum of the expected values and the observed values must be equal
observed = np.array([30,60,70,40])
chi_squared,p_value = st.chisquare(observed,expected)
print(p_value)

# as the p_value is greater than the significant level or alpha, so we cannot reject the null hypothesis