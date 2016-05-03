import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate

cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip('months')))
loansData['Loan.Length'] = cleanLoanLength

loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']
#print(intrate)

# The dependent variable
y = np.matrix(intrate).transpose()
#print(y)

#The independent variables shaped as columns
x3 = np.matrix(fico)
print(x3)
x1 = np.matrix(fico).transpose()
print(x1)
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])
print(x)

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print(f.summary())

# plt.figure()
# p = loansData['FICO.Score'].hist()
# plt.show()

# plt.figure()
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
# plt.show()

# plt.figure()
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
# plt.show()