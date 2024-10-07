import pandas as pd

df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], columns= ['A', 'B', 'C'], index= ['x', 'y', 'z'])
print(df.head())
