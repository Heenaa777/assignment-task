#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Customer ID - Unique identifier for each customer
Age - Age of the customer
Gender - Gender of the customer (Male/Female)
Item Purchased - The item purchased by the customer
Category - Category of the item purchased
Purchase Amount (USD) - The amount of the purchase in USD
Location - Location where the purchase was made
Size - Size of the purchased item
Color - Color of the purchased item
Season - Season during which the purchase was made
Review Rating - Rating given by the customer for the purchased item
Subscription Status - Indicates if the customer has a subscription (Yes/No)
Shipping Type - Type of shipping chosen by the customer
Discount Applied - Indicates if a discount was applied to the purchase (Yes/No)
Promo Code Used - Indicates if a promo code was used for the purchase (Yes/No)
Previous Purchases - The total count of transactions concluded by the customer at the store, excluding the ongoing transaction
Payment Method - Customer's most preferred payment method
Frequency of Purchases - Frequency at which the customer makes purchases (e.g., Weekly, Fortnightly, Monthly)


# In[2]:


import pandas as pd 
import numpy as np


# In[84]:


df = pd.read_excel(r"C:\Users\heena\Downloads\shopping.xlsx")


# In[85]:


df.head()


# ### Missing values

# In[86]:


df.drop("Customer ID",axis = 1,inplace = True)


# In[87]:


df.isna().sum()


# In[88]:


df["Age"].fillna(40,inplace=True)
df["Gender"].fillna(df["Gender"].mode()[0],inplace = True)
df["Item Purchased"].fillna(df["Item Purchased"].mode()[0],inplace = True )
df["Category"].fillna(df["Category"].mode()[0],inplace = True)
df["Location"].fillna(df["Location"].mode()[0],inplace = True)
df["Location"].fillna(df["Location"].mode()[0],inplace = True)
df["Color"].fillna(df["Color"].mode()[0],inplace = True)
df["Season"].fillna(df["Season"].mode()[0],inplace = True)
df["Review Rating"].fillna(df["Review Rating"].median(),inplace = True)
df["Subscription Status"].fillna(method = "ffill",inplace = True)
df["Discount Applied"].fillna(method = "bfill",inplace = True)
df["Promo Code Used"].fillna(method = "ffill",inplace = True)
df["Payment Method"].fillna(method = "bfill",inplace = True)
df["Frequency of Purchases"].fillna(method = "ffill",inplace = True)


# In[89]:


df.isnull().sum()


# ### outliers

# In[76]:


age = (df["Age"]<0)|(df["Age"]>100)


# In[77]:


sum((df["Age"]<0)|(df["Age"]>100))


# In[41]:


df["Age"] = np.where(age,30,df["Age"])


# In[43]:


df[(df["Age"]<0)|(df["Age"]>100)] # there is no outliers


# In[79]:


rev = (df["Review Rating"]<0)|(df["Review Rating"]>5)


# In[80]:


sum((df["Review Rating"]<0)|(df["Review Rating"]>5))


# In[81]:


df["Review Rating"] = np.where(rev,5,df["Review Rating"])


# ## type casting

# In[57]:


df.info()


# In[58]:


df["Age"] = df["Age"].astype("float16")


# In[59]:


df["Review Rating"]  = df["Review Rating"].astype("float16")


# In[60]:


df["Purchase Amount (USD)"] = df["Purchase Amount (USD)"].astype("int8")


# In[63]:


df["Previous Purchases"] = df["Previous Purchases"].astype("int8")


# In[64]:


df.info()


# ## duplicate values

# In[68]:


df.duplicated().sum() # duplicates cleared


# In[67]:


df.drop_duplicates(inplace = True)


# ## Variance

# In[90]:


df.head()


# In[91]:


df['Age'].var()


# In[98]:


df["Gender"].unique


# In[96]:


df["Gender"].nunique() # var =0


# In[99]:


df.drop("Gender",axis = 1,inplace = True)


# In[100]:


df.columns


# In[101]:


df['Item Purchased'].nunique()


# In[102]:


df['Category'].nunique()


# In[103]:


df["Purchase Amount (USD)"].nunique()


# In[112]:


df['Review Rating'].var()


# In[106]:


df['Season'].nunique()


# In[107]:


df['Subscription Status'].nunique()


# In[110]:


df['Subscription Status'].nunique()


# In[111]:


df['Discount Applied'].nunique()


# In[113]:


df['Previous Purchases'].var()


# ## one hot encoding and dummy variable

# In[125]:


df.head()


# In[116]:


pd.get_dummies(df["Item Purchased"],dtype = "int") # one hot encoding method converting textual data into numerica data


# In[117]:


pd.get_dummies(df["Category"],dtype = "int")


# In[124]:


pd.get_dummies(df["Location"],dtype = "int")


# In[126]:


pd.get_dummies(df["Color"],dtype = "int")


# In[127]:


pd.get_dummies(df["Size"],dtype = "int")


# In[130]:


pd.get_dummies(df["Shipping Type"],dtype = "int",drop_first = True) # dummy variable trap


# In[129]:


pd.get_dummies(df["Payment Method"],dtype = "int")


# # scaling

# In[131]:


df.head()


# In[132]:


df["Age"].mean(),df["Age"].median() 


# In[134]:


df["Age"].isna().sum() # there is no missing values


# In[136]:


def normal(x):
    n = (x-df['Age'].min())/((df['Age'].max())-(df['Age'].min()))
    return n


# In[137]:


df["Age"].apply(normal)


# In[138]:


df["Purchase Amount (USD)"].mean(),df["Purchase Amount (USD)"].median()


# In[139]:


def normal(x):
    n = (x-df["Purchase Amount (USD)"].min())/((df["Purchase Amount (USD)"].max())-(df["Purchase Amount (USD)"].min()))
    return n


# In[143]:


df['Purchase Amount (USD)'].apply(normal),df['Purchase Amount (USD)'] # label encoding


# In[ ]:




