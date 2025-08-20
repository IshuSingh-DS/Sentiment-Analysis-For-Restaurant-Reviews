import pandas as pd

df = pd.read_csv('Restaurant_Reviews.tsv', sep='\t')
print(df.shape)
