from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/chris/OneDrive/Documents/GitHub/CSIS-497/Module 1/Demo/regress_test.csv')

# print(data)

data.plot(kind='scatter', x='Bus_Age_Years', y='Maintenance_Cost', color='red')
data.hist()

# plt.show()

slope, intercept, r, p, std_err = stats.linregress(data["Bus_Age_Years"], data["Maintenance_Cost"])

print("Slope: ", slope)
print("Intercept: ", intercept)
print("R-squared: ", r ** 2)
print("p-value: ", p)