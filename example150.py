import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
sns.boxplot(x='time', y='tip', data=tips, hue='sex')
plt.show()