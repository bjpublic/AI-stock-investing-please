print(df[(df['year'] > df['year'].mean()) | (df['country'] == 'Afghanistan')])