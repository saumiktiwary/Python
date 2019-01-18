
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import csv
from pandas import ExcelWriter
import pandas as pd
url=input()


# In[2]:


website_url = requests.get(url).text


# In[3]:


soup = BeautifulSoup(website_url,'lxml')
print(soup.prettify())


# In[5]:


My_table = soup.find('table',{'class':'wikitable sortable'})
My_table
list_of_rows = []
for row in My_table.findAll('tr')[0:]:
	list_of_cells = []
	for cell in row.findAll('td'):
		text = cell.text.replace('&nbsp;','')
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)


# In[6]:


df = pd.DataFrame()
df = list_of_rows
writer = ExcelWriter("C:\\Users\Saumik\Desktop\smoke1.xlsx")
pd.DataFrame(df).to_excel(writer,sheet_name='Sheet1', index=False, engine='xlsxwriter')
writer.save()


# In[ ]:




