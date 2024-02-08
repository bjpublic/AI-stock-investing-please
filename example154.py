import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tips = sns.load_dataset("tips")
tips[['total_bill', 'tip']].plot.hist(bins=20, alpha = 0.5)
plt.show()