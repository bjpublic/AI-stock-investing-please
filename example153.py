import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tips = sns.load_dataset("tips")
tips['total_bill'].plot.hist()
plt.show()