# In[2]:

from bs4 import BeautifulSoup
import requests

# In[5]:


url = 'https://www.worldometers.info/world-population/population-by-country/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[6]:


print(soup)


# In[9]:


table = soup.find('table', 'table table-striped table-bordered')


# In[11]:


table.find_all('th')


# In[12]:


world_columns = table.find_all('th')


# In[15]:


world_column_titles = [columns.text for columns in world_columns]
print(world_column_titles)


# In[16]:


import pandas as pd

df = pd.DataFrame(columns = world_column_titles)
df


# In[17]:


table.find_all('td')


# In[18]:


table.find_all('tr')


# In[21]:


world_rows = table.find_all('tr')


# In[23]:


for row in world_rows:
     row_data = row.find_all ('td')
     individual_row_data = [data.text for data in row_data]

print(individual_row_data)


# In[25]:


for row in world_rows[1:]:
    row_data = row.find_all ('td')
    individual_row_data = [data.text for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

df

df

df.to_csv(r'C:\Users\Dzefro\Desktop\Analyst Builder\Python\P4_World_Population_Scraped.csv', index = False)






