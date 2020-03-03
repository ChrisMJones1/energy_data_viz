import pandas as pd
import numpy as np

import pyarrow

from datetime import datetime

# outdoor temp
df = pd.read_json ('data/outdoortemp.json', orient='columns')
df = df.transpose()

print(df)

parquetdataname = "data/outdoortemp.parquet"

df.to_parquet(parquetdataname)

# exhaust temp
df = pd.read_json ('data/exhaustairtemp.json', orient='columns')
df = df.transpose()

print(df)

parquetdataname = "data/exhausttemp.parquet"

df.to_parquet(parquetdataname)

# supply temp

df = pd.read_json ('data/supplyairtemp.json', orient='columns')
df = df.transpose()

print(df)

parquetdataname = "data/supplytemp.parquet"

df.to_parquet(parquetdataname)

# volume rate

df = pd.read_json ('data/volumerate.json', orient='columns')
df = df.transpose()

print(df)

parquetdataname = "data/volumerate.parquet"

df.to_parquet(parquetdataname)

# energy rate

df = pd.read_json ('data/energyrate.json', orient='columns')
df = df.transpose()

print(df)

parquetdataname = "data/energyrate.parquet"

df.to_parquet(parquetdataname)