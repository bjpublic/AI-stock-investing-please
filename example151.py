import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
sns.lmplot(x='total_bill', y='tip', data=tips, fit_reg=False, hue='sex', col = 'time')
plt.show()