import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)


df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
print(df2)

# Viewing data
print(df2.dtypes)
print(dir(df2))

print(df.head())
print(df.tail(3))
print(df.index)
print(df.values)
print(df.describe())

print(df.T)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by='B'))sort_values(by='B'))

# Selection
print(df['A'])

print(type(df['A']))
print(df[0:3])
print(df['20130102':'20130104'])

print(df.loc[dates[0]])
print(df.loc['20130102'])
print(df.loc['2013-01-02'])

print(df.mean())




