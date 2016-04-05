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

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

def IR_TF(x):
	if x['Interest.Rate'] < 0.12:
		return 0
	else:
		return 1

loansData['IR_TF'] = loansData.apply(IR_TF, axis=1)

loansData['Intercept'] = 1.0

ind_vars = ['Amount.Requested', 'FICO.Score', 'Intercept']

logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])
result = logit.fit()
coeff = result.params
print(coeff)

def logistic_function (coeff):
	p = 1/(1 + math.e**(coeff['Intercept'] + coeff['FICO.Score']*fico - coeff['Amount.Requested']*loanamt))
	return p

# print(logistic_function(coeff))

# x = np.logistic_function(coeff)
# y = np.linspace(0,1)

# y = np.linspace(0, 1, 100)

# plt.plot(y, y, label='linear')

# plt.show()

#print(loansData[loansData['Interest.Rate'] == 10].head())
#loansData.to_csv('loansData_clean.csv', header=True, index=False)