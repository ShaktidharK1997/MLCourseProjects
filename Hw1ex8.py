#!/usr/bin/env python
# coding: utf-8

# # Computation using numpy functions

# In[28]:


import numpy as np


# Upload the `data.csv` file to this workspace, then read in the data to a `numpy` array in `x`. If you want to, you can add code to the following cell to explore `x` (for example, see its shape).
# 

# In[29]:


x = np.genfromtxt('data.csv',delimiter=',')


# Create an empty `numpy` array called `grades`, with the same shape as `x`, which will hold string values:

# In[30]:


grades = np.empty(shape=x.shape, dtype='str')


# Write code to compute the letter grade (A, B, or C) for all students, and assign the results to the `grades` array. There should be a one-to-one correspondence between `x` and `grades`, i.e. the 10th entry in `x` should correspond to the same student as the 10th entry in `grades`.

# In[39]:


#grade (write your code in this cell and DO NOT DELETE THIS LINE)
rank_x=np.argsort(x,axis=0)
length = len(x)
cindex = int(length*0.15)
bindex = int(length*0.65)
grades[rank_x[0:cindex]] = 'C'
grades[rank_x[cindex:bindex]] = 'B'
grades[rank_x[bindex:]] = 'A'


# Then, write code to find out the minimum numeric score that got an A, and the minimum numeric score that got a B, and assign these values to `a_min` and `b_min`, respectively:

# In[40]:


#grade (write your code in this cell and DO NOT DELETE THIS LINE)
a_min = x[rank_x[bindex]]
b_min = x[rank_x[cindex]]


# In[37]:





# In[ ]:




