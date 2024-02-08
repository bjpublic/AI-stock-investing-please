import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
sns.countplot(x=tips['day'], data=tips)
plt.show()