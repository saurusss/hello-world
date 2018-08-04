points = [ { 'x' : 2, 'y' : 3 },
{ 'x' : 4, 'y' : 1 } ]
points.sort(key=lambda i : i['y'])
print(points)

# dataframe 연습
import pandas as pd
pdf = pd.DataFrame(points)
print(pdf)