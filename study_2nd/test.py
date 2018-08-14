import tensorflow as tf
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import random
# %matplotlib inline

df = pd.DataFrame(columns=['x', 'y'])
for i in  range(31):
    df.loc[i] = [random.randrange(1,18), random.randrange(1,18)]
print(df ) 
sb.lmplot('x', 'y',data =df, fit_reg=False, scatter_kws = {"s":100} )
plt.title('K-means Example')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

points = df.values

kmeans = KMeans(n_clusters=4).fit(points)
kmeans.cluster_centers_