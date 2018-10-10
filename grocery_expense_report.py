
# coding: utf-8

# In[28]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[59]:


get_ipython().system('pwd')


# In[4]:


dfs = pd.read_excel('Grocery.xlsx', sheet_name=None)


# In[9]:


dfs.keys()


# In[10]:


veggie = dfs['Veggie']
meat = dfs['Meat']
baking = dfs['Baking Supply']
supplement = dfs['supplement']
bread = dfs['Bread']
others = dfs['Others']
fruit = dfs['Fruit']


# ### veggie

# In[11]:


veggie.Amount.sum()


# In[57]:


veggie.groupby('Veggie Name').sum().sort_values('Amount', ascending=False)[:6]['Amount'].sum()


# In[37]:


veggie.groupby('Veggie Name').sum().sort_values('Amount', ascending=False)      .plot(kind='bar', grid=True, figsize=(12,8))


# ### meat

# In[38]:


meat.Amount.sum()


# In[40]:


meat.groupby('Meat Name').sum().sort_values('Amount', ascending=False)      .plot(kind='bar', grid=True, figsize=(12,8))


# ### baking

# In[41]:


baking.Amount.sum()


# In[46]:


supplement


# In[47]:


89.99+7.19


# In[48]:


bread.Amount.sum()


# ### others

# In[49]:


others.Amount.sum()


# In[51]:


others.groupby('Name').sum().sort_values('Amount', ascending=False)[:10]


# ### fruit

# In[52]:


fruit.Amount.sum()


# In[53]:


veggie.Amount.sum() + meat.Amount.sum() + others.Amount.sum() + others.Amount.sum() + fruit.Amount.sum() + 97.2

