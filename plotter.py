from matplotlib import pylab as plt
import numpy as np
import math
import pandas as pd

data = pd.read_csv("generated.csv")
df = pd.DataFrame(data)
data_dict = df.to_dict(orient="split")

x_labels = [d[0] for d in data_dict['data']]
bed_places = [b[1] if not math.isnan(b[1]) else 0 for b in data_dict['data']]
internet_users = [u[2] if not math.isnan(u[2]) else 0.0 for u in data_dict['data']]

fig = plt.figure(figsize=(25,10))
ax = fig.add_axes([0.1,0.1,0.75,0.75])
ax.bar(x_labels, bed_places, width=0.4, color='r')
ax.set_xlabel("Country Codes", fontsize="20", fontstyle="italic")
ax.set_ylabel("Number of Bed-places", fontsize="20", fontstyle="italic")
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
fig.savefig("bedplaces.png")

fig2 = plt.figure(figsize=(25,10))
ax2 = fig2.add_axes([0.1,0.1,0.75,0.75])
ax2.bar(x_labels, internet_users, width=0.4, color='b')
ax2.set_xlabel("Country Codes", fontsize="20", fontstyle="italic")
ax2.set_ylabel("Percentage of individuals online", fontsize="20", fontstyle="italic")
ax2.tick_params(axis='x', labelsize=20)
ax2.tick_params(axis='y', labelsize=20)
fig2.savefig("internetusers.png")