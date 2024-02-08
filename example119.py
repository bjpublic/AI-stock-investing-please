import pandas as pd

site = pd.read_csv("site.csv")
visited = pd.read_csv("visited.csv")

result = visited.merge(site, left_on = "site", right_on = 'name')
print(result)