import pandas as pd
import numpy as np
import json 
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder

train_data = pd.read_csv(r"F:\chatbot\training_data.csv")
chatbot = load_model("F:\chatbot")
responses = json.load(open("responses.json", "r"))

train_data["patterns"] = train_data["patterns"].str.lower()
vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
vectorizer.fit(train_data["patterns"])

le = LabelEncoder()
le.fit(train_data["tags"])

bot_name = "CHAPPIE"

def predict_tag(inp_str):
    inp_data_tfid = vectorizer.transform([inp_str.lower()]).toarray()
    predicted_prob = chatbot.predict(inp_data_tfid)
    encoded_label = [np.argmax(predicted_prob)]
    predicted_tag = le.inverse_transform(encoded_label)[0]
    return predicted_tag

def start_chat(inp_msg):
    
    while(True):
        if inp_msg == "EXIT":
            break
        else:
            if inp_msg:
                tag = predict_tag(inp_msg)
                return random.choice(responses[tag])
            else:
                return "Sorry ! I do not understand."
            