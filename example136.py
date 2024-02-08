import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.hist(tips['total_bill'], bins=10)

ax.set_title("Histogram")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Freq")

plt.show()