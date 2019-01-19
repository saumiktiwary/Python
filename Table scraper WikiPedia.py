
# coding: utf-8

# In[17]:


import pandas as pd
from pandas import ExcelWriter
tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_countries_by_cigarette_consumption_per_capita#2016_rankings")
print("Enter the table number in order you want to check")
x=int(input())
writer = ExcelWriter("C:\\Users\Saumik\Desktop\Table.xlsx")
pd.DataFrame(tables[0]).to_excel(writer,sheet_name='Sheet1', index=False, engine='xlsxwriter')
writer.save()


# In[ ]:





# In[ ]:




