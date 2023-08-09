#!/usr/bin/env python
# coding: utf-8

# # Q1
#  Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.

# In[1]:


import pandas as pd


# In[6]:


pan_ser=pd.Series([4,8,15,16,23,42])


# In[7]:


print(pan_ser)


# Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
# variable print it.

# In[12]:


Var_list = [1,2,'data','sem','xrd',55,35,'MATLAB','Battery',99]


# In[13]:


df=pd.Series(Var_list)


# In[14]:


print(df)


# Q3. Create a Pandas DataFrame that contains the following data:

# In[1]:


import pandas as pd


# In[2]:


dataframe= [['Alice',25,'Female'],['Bob',30,'Male'],['Claire',27,'Female']]


# In[7]:


new_df = pd.DataFrame(dataframe,columns=['Name','Age','Gender'])


# In[9]:


new_df


# # Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

# # Dataframe:
# A dataframe is a 2 Dimensional data structure, like a 2D Array, or a table with columns and rows. So basically it is a structured form of Data. Where as a series is column in a table.
# 

# In[16]:


#example of Dataframe 
dats = [['ABC','Mtech',24],['XYZ','Btech',25]]


# In[17]:


df2=pd.DataFrame(dats,columns=['Name','Degree Course','Passing Year'])
df2


# In[25]:


#example of series
df2['Degree Course']


# In[23]:


type(df2['Degree Course'])


# In[24]:


type(df2)


# Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# you give an example of when you might use one of these functions?

# Some common functions are
# head() : Allows you to see first 5 rows of given Dataframe
# tail() : Allows you to see last 5 rows of given DataFrame

# In[27]:


df9=pd.read_csv("Services.csv")


# In[28]:


df9


# In[29]:


df9.head()


# In[30]:


df9.tail()


# In[32]:


df9.shape
#this returns the number of rows and columns


# Q6. Which of the following is mutable in nature Series, DataFrame, Panel?

# Series, Dataframe and Panel are mutable in nature.
# In dataframe we can add the columns also we can modify the existing columns
# In series objects are mutable we can modify their values after creation.
# Panels : In new version of Pandas the panel data structure has been deprecated and no longer in use.
# 

# Create a DataFrame using multiple Series. Explain with an example.

# In[34]:


#creating a dataframe
import pandas as pd

Nf_Data = [['Frozen Rays',10000,2022],['SNI',15840,2023],['Drexity',6000,2023]]


# In[38]:


dp=pd.DataFrame(Nf_Data,columns=['Artist Name','Spotify Monthly Listeners','Year'])


# In[39]:


#showing the data frame
dp


# In[40]:


dp.columns


# In[42]:


dp[['Artist Name','Spotify Monthly Listeners']]


# Pandas aligned the Series based on their index values, resulting in a coherent DataFrame where each row corresponds to an Artist, and each column represents a specific attribute of an Artist. 

# In[ ]:




