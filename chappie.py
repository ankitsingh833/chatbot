#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import save_model


# In[2]:


train_data = pd.read_csv(r'F:\chatbot\training_data.csv')


# In[3]:


train_data['patterns'] = train_data['patterns'].str.lower()
vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
train_data_tfidf = vectorizer.fit_transform(train_data['patterns']).toarray()


# In[4]:


lab_enc = LabelEncoder()
tags_lab_enc = pd.DataFrame({"tags": lab_enc.fit_transform(train_data["tags"])})
tags_dummy_enc = pd.get_dummies(tags_lab_enc["tags"]).to_numpy()


# In[5]:


def chappie(model, inp_shape):
    chatbot = model
    chatbot.add(Dense(16, input_shape = inp_shape))
    chatbot.add(Dense(18))
    chatbot.add(Dense(16))
    chatbot.add(Dense(12))
    chatbot.add(Dense(len(tags_dummy_enc[0]), activation = 'softmax'))
    return chatbot


# In[6]:


chatbot = chappie(Sequential(), (len(train_data_tfidf[0]), ))


# In[7]:


chatbot.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])


# In[8]:


chatbot.fit(train_data_tfidf, tags_dummy_enc, epochs = 100, batch_size = 32, verbose = 0)


# In[9]:

FILE = "F:\chatbot"
save_model(chatbot, FILE)

