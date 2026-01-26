import pandas as pd
import numpy as np
from scipy.stats import norm , t

population_mean = 72  #given from question
alpha = 0.05

df = pd.read_csv("C:/Users/ashok/Downloads/chapter12_assets/chapter12_assets/12_2_case_study_exam_score/exam_scores.csv")
print(df)
print(df.shape)

n=df.shape[0]  #sample size
degree_of_freedom =n-1
print(degree_of_freedom)

sample_mean = df.score.mean()
sample_std = df.score.std()
print(sample_std)
print(sample_mean)