#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


url = 'https://bigsr.africa/category/big-saturday-read/page/'


# In[3]:


article_urls = set()

for page in range(1,17):

    # Concatenate to get new page URL
    page_url = url+str(page)
    # Obtain Request
    res = requests.get(page_url)
    # Turn into Soup
    soup = BeautifulSoup(res.text,'lxml')
    
    containers = soup.findAll("h3", attrs={"class": "entry-title td-module-title"})
    #print(content)
    for div in containers:
        links = div.findAll('a')
        for a in links:
            article_urls.add(a['href'])
    #print(soup)


# In[25]:


for url in article_urls:
    
    #Obtain Request
    res = requests.get(url)
    # Turn into Soup
    soup = BeautifulSoup(res.text,'lxml')
    
    heading  = soup.findAll("h1", attrs = {"class": "entry-title"})
    for i in heading:
        name = i.text.replace(':','_').replace('?','')
        
        
    post_date  = soup.findAll("span", attrs = {"class": "td-post-date"})
    for date in post_date[0]:
        date = date.text
        
        
    views  = soup.findAll("div", attrs = {"class": "td-post-views"})
    for view in views:
        v = view.text
        
    body  = soup.findAll("div", attrs = {"class": "td-post-content tagdiv-type"})
    for par in body:
        par = par.text
    
    try:
        with open(f'{name}.txt', 'w',encoding='utf-8') as f:
                #print(name)
                f.write(name)
                f.write(f' Published{date}.')
                f.write('/n')
                f.write(f' {v} views.')
                f.write(par)
    except Exception as e:
        print(e)
        continue


# In[ ]:





# In[ ]:




