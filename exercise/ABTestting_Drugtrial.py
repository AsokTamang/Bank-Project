import pandas as pd
df_control = pd.read_csv("C:/Users/ashok/Downloads/chapter10_assets/chapter10_assets/11_z_test_AB_testing_coding/control_group.csv")
print(df_control)

df_test = pd.read_csv("C:/Users/ashok/Downloads/chapter10_assets/chapter10_assets/11_z_test_AB_testing_coding/test_group.csv")
print(df_test)

control_mean = df_control.recovery_time_hrs.mean()
control_std = df_control.recovery_time_hrs.std()
print(control_mean)
print(control_std)