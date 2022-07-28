import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'medium',
          #'figure.figsize': (15, 5),
          'axes.labelsize': 'medium',
          'axes.titlesize':'medium',
          'xtick.labelsize':10,
          'ytick.labelsize':10}
pylab.rcParams.update(params)


df1 = pd.DataFrame(np.random.rand(8, 8))
df2 = pd.DataFrame(np.random.rand(8, 8))

x_axis_labels = [1,2,3,4,5,6,7,8]
y_axis_labels = [1,2,4,8,16,32,64,128]

fig, (ax1, ax2) = plt.subplots(ncols=2)
fig.subplots_adjust(wspace=0.02)  # space between two subplots

# first heatmap
s1 = sns.heatmap(df1, cmap="hot", ax=ax1, cbar=False, square=True, 
	xticklabels=x_axis_labels,
	yticklabels=y_axis_labels
	) # cbar_kws={'shrink': 0.6}
s1.set(xlabel="Number of Models", ylabel="Batch Size", title="Throughput")
fig.colorbar(ax1.collections[0], ax=ax1, location="left", 
	use_gridspec=False, pad=0.3, shrink=0.4)

# second heatmap
s2 = sns.heatmap(df2, cmap="hot", ax=ax2, cbar=False, square=True, 
	xticklabels=x_axis_labels,
	yticklabels=y_axis_labels
	)
s2.set(xlabel="Number of Models", ylabel="Batch Size", title="Latency")
fig.colorbar(ax2.collections[0], ax=ax2, location="right", 
	use_gridspec=False, pad=0.3, shrink=0.4)

ax2.yaxis.set_label_position("right")
ax2.yaxis.tick_right()
ax1.tick_params(rotation=0)
ax2.tick_params(rotation=0)

plt.show()