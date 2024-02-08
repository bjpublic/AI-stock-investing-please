import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.scatter(tips['total_bill'], tips['tip'], c = tips['size'], s = tips['size'] * 20, alpha = 0.5)
ax.set_title("Scatter Plot")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")

plt.show()