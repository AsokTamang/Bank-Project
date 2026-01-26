import pandas as pd
import numpy as np
from scipy.stats import norm , t

population_mean = 72  #given from question

df = pd.read_csv("C:/Users/ashok/Downloads/chapter12_assets/chapter12_assets/12_2_case_study_exam_score/exam_scores.csv")
print(df)
print(df.shape)

