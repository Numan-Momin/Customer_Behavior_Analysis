#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
df = pd.read_csv(r'C:\Users\momin\Downloads\shopping_behavior_updated (2).csv')


# In[13]:


df.head()


# In[14]:


df.info()


# In[16]:


df.describe(include='all')


# In[17]:


df.isnull().sum()


# In[22]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[23]:


df.columns


# In[25]:


# create a column age_group
labels=['Young Adult','Adult','Middle-aged','Senior']
df['age_group']= pd.qcut(df['age'],q=4, labels=labels)


# In[26]:


df[['age','age_group']].head(10)


# In[31]:


# create column purchase_frequency_days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quaterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
    }
df['purchase_frequency_days']= df['frequency_of_purchases'].map(frequency_mapping)


# In[32]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[33]:


df[['discount_applied','promo_code_used']].head(10)


# In[36]:


(df['discount_applied'] == df['promo_code_used']).all()


# In[37]:


df = df.drop('promo_code_used',axis = 1)


# In[39]:


df.columns


# In[41]:


pip install psycopg2-binary sqlalchemy


# In[49]:


from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "postgres"
password = "Postgres@123"
host = "localhost"
port = "5432"
database = "customer_behavior"

# Encode password safely
encoded_password = quote_plus(password)

engine = create_engine(
    f"postgresql+psycopg2://{username}:{encoded_password}@{host}:{port}/{database}"
)

# Load DataFrame
table_name = "customer"

df.to_sql(
    table_name,
    engine,
    if_exists="replace",
    index=False
)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")


# In[ ]:





# In[ ]:




