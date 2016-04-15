import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import math as math

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate

cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip('months')))
loansData['Loan.Length'] = cleanLoanLength

loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]

loansData['Annual.Income'] = loansData['Monthly.Income'].map(lambda val: val*12)

def H_O(x):
	if x['Home.Ownership'] == 'RENT':
		return 0
	elif x['Home.Ownership'] == 'MORTGAGE':
		return 1
	else:
		return 2

loansData['H_O'] = loansData.apply(H_O, axis=1)

intrate = loansData['Interest.Rate']
income = loansData['Annual.Income']
home_ownership = loansData['H_O']

# The dependent variable
y = np.matrix(intrate).transpose()
#print(y)

#The independent variables shaped as columns
x1 = np.matrix(income).transpose()
# print(x1)
x2 = np.matrix(home_ownership).transpose()

x = np.column_stack([x1])
# print(x)

# plt.figure()
# plt.scatter(x,y, alpha=0.05)
# plt.show()

X = sm.add_constant(x)
model = sm.OLS(y,X, missing='drop')
f = model.fit()

print(f.summary())