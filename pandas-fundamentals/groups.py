import pandas as pd
import numpy as np


df = pd.read_pickle('data_frame.pickle')

# ITERATION
# make a copy of a smaller fdataset
small_df = df.iloc[49980:50019, :].copy()
grouped = small_df.groupby('artist')
# type(grouped)

for name, group_df in grouped:
    print(name)
    print(group_df)
    break  # print only the first group

# Aggregate
# Mins
for name, group_df in small_df.groupby('artist'):
    min_year = group_df['acquisitionYear'].min()
    print("{}: {}".format(name, min_year))


# Transform
# Equivalent of editing by hand:
# Make a case when there is no data to infer
# small_df.loc[[11838, 16441], 'medium'] = np.nan
def fill_values(series):
    values_counted = series.value_counts()
    if values_counted.empty:
        return series
    most_frequent = values_counted.index[0]
    new_medium = series.fillna(most_frequent)
    return new_medium


def transform_df(source_df):
    group_dfs = []
    for name, group_df in source_df.groupby('artist'):
        filled_df = group_df.copy()
        filled_df.loc[:, 'medium'] = fill_values(group_df['medium'])
        group_dfs.append(filled_df)

    new_df = pd.concat(group_dfs)
    return new_df


# Now check the result
filled_df = transform_df(small_df)

# BUILT-INS
# Transform
grouped_mediums = small_df.groupby('artist')['medium']
small_df.loc[:, 'medium'] = grouped_mediums.transform(fill_values)

# Min
df.groupby('artist').agg(np.min)
df.groupby('artist').min()

# Filter
grouped_titles = df.groupby('title')
title_counts = grouped_titles.size().sort_values(ascending=False)

condition = lambda x: len(x.index) > 1
dup_titles_df = grouped_titles.filter(condition)
dup_titles_df.sort_values('title', inplace=True)
