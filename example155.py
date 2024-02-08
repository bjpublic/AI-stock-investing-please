import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tips = sns.load_dataset("tips")
tips.plot.box()
plt.show()