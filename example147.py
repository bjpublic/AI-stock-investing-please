import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
sns.violinplot(x='time', y='total_bill', data=tips)
plt.show()