import pandas as pd


# Let's load the data for the first time
df = pd.read_pickle('data_frame.pickle')

# df.artist - not recommended
artists = df['artist']
pd.unique(artists)

# number of artists without looking at duplicates
number_of_artists = len(pd.unique(artists))

# check where artist is bacon, sets to either true or false depending
s = df['artist'] == 'Bacon, Francis'
bacon_appearences = s.value_counts()  # count number of truthy values
num_of_bacon_appearences = bacon_appearences[True]

# Other way
# artist_counts = df['artist'].value_counts()
# artist_counts['Bacon, Francis']

# row id 1035 and column artist
print(df.loc[1035, 'artist'])

# all rows where bacon is the artist
print(df.loc[df['artist'] == 'Bacon, Francis', 'artist'])

# iloc in for strictly index values (row, column)
df.iloc[0, 0]
df.iloc[0, :]
df.iloc[0:2, 0:2]

# # Try multiplication
# df['height'] * df['width'] - does not work
# df['width'].sort_values().head()
# df['width'].sort_values().tail()

# # Try to convert
# pd.to_numeric(df['width']) - errors when it encounters nun-numeric values

# # Force NaNs
# change to numeric values, if something is not a number, change it to NaN
pd.to_numeric(df['width'], errors='coerce')

# replace non-numeric values to Nan to allow for computation
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')

area = df['height'] * df['width']
# Assign - create new columns with size,
# area(name of column) = area(calculation formulae) the variable hapa juu
df = df.assign(area=area)

df['area'].max()  # get highest value
df['area'].idxmax()  # get the index of the highest value as well
df.loc[df['area'].idxmax(), :]

# try as much as possible to stick to loc and iloc
