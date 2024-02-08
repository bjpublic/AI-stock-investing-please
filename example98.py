import pandas as pd

df = pd.read_csv("gapminder.tsv", sep = '\t')

lifeExp = df['lifeExp']
print(lifeExp)