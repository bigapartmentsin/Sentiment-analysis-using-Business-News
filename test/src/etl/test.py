import pandas as pd

df=pd.read_csv('../../TCS_score_open.csv')

print(df.head(1))

df=pd.read_csv('../../REL_sentiment.csv')

print(df.describe())

df=df.set_index('date')

print(df.head(2))

