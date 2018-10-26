import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

df = pd.read_pickle('data_frame.pickle')

# Simplest default plot
acquisition_years = df.groupby('acquisitionYear').size()

# print(acquisition_years.sort_values().tail())

# acquisition_years.plot()  # plot using in-built matplotlib in pandas


# started using imported matplotlib rather than the matplotlib  in pandas

rcParams.update({'figure.autolayout': True, 'axes.titlepad': 20})

fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
acquisition_years.plot(ax=subplot)

# Add axis labels
subplot.set_xlabel("Acquisition Year")
subplot.set_ylabel("Artworks Acquired")

# Increase ticks granularity
subplot.locator_params(nbins=40, axis='x')

# Rotate X ticks
acquisition_years.plot(ax=subplot, rot=45)

# Add log scale
acquisition_years.plot(ax=subplot, rot=45, logy=True)

# Add grid
acquisition_years.plot(ax=subplot, rot=45, logy=True, grid=True)

# Set fonts
title_font = {
    'family': 'source sans pro',
    'color': 'darkblue',
    'weight': 'normal',
    'size': 20,
}
labels_font = {
    'family': 'consolas',
    'color': 'darkred',
    'weight': 'normal',
    'size': 16,
}

# final plot
fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
acquisition_years.plot(ax=subplot, rot=45, logy=True, grid=True)
subplot.set_xlabel("Acquisition Year", fontdict=labels_font, labelpad=10)
subplot.set_ylabel("Artworks Acquired", fontdict=labels_font)
subplot.locator_params(nbins=40, axis='x')
subplot.set_title("Tate Gallery Acquisitions", fontdict=title_font)
fig.show()

# Save to files
# fig.savefig('plot.png')

# allows for good scalable image that you can even share online
fig.savefig('plot.svg', format='svg')
