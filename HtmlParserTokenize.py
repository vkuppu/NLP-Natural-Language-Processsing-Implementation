#!/usr/bin/env python
# coding: utf-8

# ### 30July 2019

# ### Snippet to pasre html and read text and create tokens.
# ### Needs few more modifications

# In[1]:


import urllib.request


# In[2]:


response = urllib.request.urlopen('file:///C:/reut2-002.html')


# In[3]:


html = response.read()


# In[5]:


#print (html)


# In[5]:


##use BeautifulSoup to clean the grabbed text like this, 


# In[7]:


from bs4 import BeautifulSoup
import urllib.request 
response = urllib.request.urlopen('file:///C:/reut2-002.html') 
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
#print (text)


# In[7]:


###convert that text into tokens by splitting the text like this,


# In[9]:


from bs4 import BeautifulSoup 
import urllib.request 
response = urllib.request.urlopen('file:///C:/reut2-002.html') 
html = response.read() 
soup = BeautifulSoup(html,"html5lib") 
text = soup.get_text(strip=True) 
tokens = [t for t in text.split()] 
#print (tokens)

