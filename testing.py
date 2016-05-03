import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv('LoanStats3b.csv', header=1, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']
loan_count_summary = loan_count_summary.reset_index(drop=True)
"""
Plot the loan data (loan_count_summary in from the previous assignment). Is the series stationary? 
If not, what would you do to transform it into a stationary series?
"""
loan_count_summary_diff = loan_count_summary.diff()
loan_count_summary_diff = loan_count_summary_diff.fillna(0)

loan_count_summary_diff = loan_count_summary_diff + 316

"""  we can even smooth it out by diving with the maximum value """

loan_count_summary_diff = loan_count_summary_diff/max(loan_count_summary_diff)

sm.graphics.tsa.plot_acf(loan_count_summary_diff)
plt.show()

sm.graphics.tsa.plot_pacf(loan_count_summary_diff)
plt.show()
