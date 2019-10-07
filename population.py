#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


countries=pd.read_csv('D:/B1/work/BigData/Exam/countries.csv')


# In[3]:


countries.head()


# In[20]:


data_2002=countries[countries['year']==2002]


# In[21]:


top_10_p=data_2002.sort_values('population',ascending=False).head(10)


# In[22]:


plt.figure(figsize=(12,6))

x=range(10)
plt.bar(x,top_10_p['population']/10**9)
plt.xticks(x,top_10_p['country'])
plt.xlabel('Countries')
plt.ylabel('Population in Billions')
plt.title('10 Most Populous Countries in 2002')
plt.show()


# In[23]:


plt.scatter(data_2002['gdpPerCapita'],data_2002['lifeExpectancy'])
plt.title('Life Expectancy vs GDP Per Capita in 2002 ')
plt.xlabel('GDP per Capita($)')
plt.ylabel('Life Expectancy')
plt.show()


# In[24]:


data_2002['gdpPerCapita'].corr(data_2002['lifeExpectancy'])


# In[25]:


from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(countries['year'],countries['gdpPerCapita'],countries['lifeExpectancy'], s=30)
plt.show()


# In[ ]:




