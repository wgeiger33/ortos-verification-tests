#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


# In[2]:


instron_nylon_no_stiffy_1 = pd.read_table("C:/Users/wgeig/Downloads/Specimen_RawData_1.csv", sep = ',', header = 5)
instron_nylon_no_stiffy_1 = instron_nylon_no_stiffy_1.drop(axis = 0, index = 0)


# In[3]:


instron_nylon_no_stiffy_1.reset_index()


# In[5]:


plt.plot(instron_nylon_no_stiffy_1['Extension'], instron_nylon_no_stiffy_1['Load'])
plt.xticks([])
plt.yticks([])
plt.xlabel('Extension')
plt.ylabel('Load')
plt.show()


# In[ ]:




