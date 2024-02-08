import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
sns.histplot(tips['total_bill'])
plt.show()