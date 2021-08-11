#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing some necessary packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[2]:


#initiate a list
question_list = []


# In[3]:


def pull_data(tag, page):
    #connect to url
    source=requests.get(f'https://stackoverflow.com/questions/tagged/{tag}?tab=newest&page={page}&pagesize=50') 
    #create soup object
    soup = BeautifulSoup(source.text,'html.parser')
    questions=soup.find_all('div',class_='question-summary')
    for item in questions:
        question = {
            'pull_tag': tag,
            'header' : item.find('a',class_='question-hyperlink').text,
            'link' :'https://stackoverflow.com'+ item.find('a',class_='question-hyperlink')['href'],
            'votes' : int(item.find('span',class_='vote-count-post').text),
            'date' : item.find('span',class_='relativetime')['title'],
            'num_answer' : item.find('div',class_=["status answered","status unanswered","status answered-accepted"]).text,
            'post_tag' : [x.text for x in item.find_all('a',class_='post-tag flex--item')],
            'ques_summary' : item.find('div',class_='excerpt').text.strip()
        }
        question_list.append(question)
    return question_list
for tag in ['python','pandas','python-3.x','diango','numpy','python-2.7','dataframe','tensorflow','dictionary','regex','beautifulsoup','machine-learning','web-scraping','skit-learn']:
    for page in range(100):
        quest = pull_data(tag,page)


# In[4]:


# save data into file using pandas
df=pd.DataFrame(question_list)
# save file to excel
# df.to_excel('Stack_Overflow_questions.xlsx')
#save file to csv
df.to_csv('Stack_Overflow_questions.csv')


# In[5]:


df.shape


# In[ ]:




