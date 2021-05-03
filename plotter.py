
# coding: utf-8

# In[2]:


from matplotlib import pylab as plt
import numpy as np
import math
import pandas as pd


# In[3]:


data = pd.read_csv("generated.csv")
df = pd.DataFrame(data)


# In[4]:


data_dict = df.to_dict(orient="split")


# In[5]:


x_labels = [d[0] for d in data_dict['data']]


# In[6]:


bed_places = [b[1] if not math.isnan(b[1]) else 0 for b in data_dict['data']]


# In[7]:


internet_users = [u[2] if not math.isnan(u[2]) else 0.0 for u in data_dict['data']]


# In[8]:


fig = plt.figure(figsize=(25,10))
ax = fig.add_axes([0.1,0.1,0.75,0.75])
ax.bar(x_labels, bed_places, width=0.4, color='r')
ax.set_xlabel("Country Codes", fontsize="20", fontstyle="italic")
ax.set_ylabel("Number of Bed-places", fontsize="20", fontstyle="italic")
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)


# In[9]:


fig.savefig("bedplaces.png")


# In[10]:


fig2 = plt.figure(figsize=(25,10))
ax2 = fig2.add_axes([0.1,0.1,0.75,0.75])
ax2.bar(x_labels, internet_users, width=0.4, color='b')
ax2.set_xlabel("Country Codes", fontsize="20", fontstyle="italic")
ax2.set_ylabel("Percentage of individuals online", fontsize="20", fontstyle="italic")
ax2.tick_params(axis='x', labelsize=20)
ax2.tick_params(axis='y', labelsize=20)


# In[11]:


fig2.savefig("internetusers.png")


# In[12]:


avg1 = 0
for bp in bed_places:
    avg1 += bp
    
avg1 /= len(bed_places)


# In[13]:


avg2 = 0
for iu in internet_users:
    avg2 += iu
    
avg2 /= len(internet_users)


# In[22]:


scale = int(avg1/avg2)


# In[23]:


feasibility_score = [ bed_places[i]*internet_users[i]/(scale*100) for i in range(len(bed_places)) ]


# In[24]:


fig3 = plt.figure(figsize=(25,10))
ax3 = fig3.add_axes([0.1,0.1,0.75,0.75])
ax3.bar(x_labels, feasibility_score, width=0.4, color='g')
ax3.set_xlabel("Country Codes", fontsize="20", fontstyle="italic")
ax3.set_ylabel("Approximate Feasibility Score", fontsize="20", fontstyle="italic")
ax3.tick_params(axis='x', labelsize=20)
ax3.tick_params(axis='y', labelsize=20)


# In[25]:


fig3.savefig("feasibility.png")

