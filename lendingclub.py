import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Funded.By.Investors')

plt.show()

loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()

#print(loansData)