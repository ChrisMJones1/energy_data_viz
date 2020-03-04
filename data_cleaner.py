import pandas as pd
import numpy as np

import pyarrow

from datetime import datetime

# mixed temp
df = pd.read_json ('data/mixedtemp.json', orient='columns')
df = df.transpose()
df = df.reset_index(drop=True)

print(df)


# outdoor temp
ddf = pd.read_json('data/outdoortemp.json', orient='columns')
ddf = ddf.transpose()
ddf = ddf.reset_index(drop=True)

df['outdoor'] = ddf["number"]
print(df)


# exhaust temp
ddf = pd.read_json ('data/exhaustairtemp.json', orient='columns')
ddf = ddf.transpose()
ddf = ddf.reset_index(drop=True)

df['exhaust'] = ddf['number']
print(df)


# supply temp

ddf = pd.read_json ('data/supplyairtemp.json', orient='columns')
ddf = ddf.transpose()
ddf = ddf.reset_index(drop=True)

df['supply'] = ddf['number']
print(df)


# volume rate

ddf = pd.read_json ('data/volumerate.json', orient='columns')
ddf = ddf.transpose()
ddf = ddf.reset_index(drop=True)
df['volume'] = ddf['number']
print(df)


# energy rate

ddf = pd.read_json ('data/energyrate.json', orient='columns')
ddf = ddf.transpose()
ddf = ddf.reset_index(drop=True)
print(ddf['number'])
df['energy'] = ddf['number']
print(df)

parquetdataname = "data/total.parquet"

df.to_parquet(parquetdataname)