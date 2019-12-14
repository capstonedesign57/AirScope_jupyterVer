#!/usr/bin/env python
# coding: utf-8

# # Intent_4

# In[14]:


import nltk
from nltk import word_tokenize


def intent(lst):
    if lst.lower() == "askflight" :
        y = 0
    elif lst.lower() == "askflight, askflightwithcost" :
        y = 1
    elif lst.lower() == "askflight, askflightwithairline" :
        y = 2
    else : # element.lower() in "askflight, askflightwithcost, askflightwithairline"
        y = 3
    return y

