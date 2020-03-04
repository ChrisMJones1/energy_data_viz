import pandas as pd
import numpy as np

import pyarrow

from datetime import datetime

df = pd.read_parquet('data/total.parquet')

df['ratio'] = (df['number'].astype(int) - df['outdoor'].astype(int) ) / (df['supply'].astype(int)  - df['outdoor'].astype(int))


print(df)
df['amountsaved'] = (df['ratio'].astype(float) * df['energy'].astype(float)) + df['energy'].astype(float)
df['amountsaved'] = df['amountsaved'].astype(int)
print(df)
summed = df['amountsaved'].sum()
print(summed)

print(str((summed / 1000000) * 114))