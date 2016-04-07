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
loansData['Annual.Income'] = loansData['Annual.Income'].astype(object)
loansData['Annual.Income'] = loansData['Monthly.Income'].map(lambda x: int(x))
print(loansData['Annual.Income'])

# def H_O(x):
# 	if x['Home.Ownership'] == 'RENT':
# 		return 0
# 	elif x['Home.Ownership'] == 'MORTGAGE':
# 		return 1
# 	else:
# 		return 2

# loansData['H_O'] = loansData.apply(H_O, axis=1)

# intrate = loansData['Interest.Rate']
# income = loansData['Annual.Income']
# home_ownership = loansData['H_O']

# loansData['Intercept'] = 1.0

# ind_vars = ['Annual.Income']

# logit = sm.Logit(loansData['Interest.Rate'], loansData[ind_vars])
# result = logit.fit()
# coeff = result.params
# print(coeff)

# def logistic_function (coeff):
# 	p = 1/(1 + math.e**(coeff['Intercept'] + coeff['FICO.Score']*fico - coeff['Amount.Requested']*loanamt))
# 	return p

# print(logistic_function(coeff))