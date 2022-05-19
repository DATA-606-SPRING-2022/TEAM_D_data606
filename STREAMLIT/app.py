# my fake news -  app.py
import streamlit as st
import joblib,os
from pathlib import Path
#importing necessary libraries 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
import pandas as pd
nltk.download('punkt')
nltk.download('wordnet')
import string
from bs4 import BeautifulSoup
import re
import pickle

#Remove stopwords:
nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('english')

# converting the textual data to numerical data
from sklearn.feature_extraction.text import TfidfVectorizer
import base64

this_folder = str(Path(__file__).parents[0])
model_file = this_folder + '\models'

def load_prediction_models(model_file):
	loaded_model = pickle.load(open((model_file),"rb"))
	return loaded_model

#setting background image
@st.cache(allow_output_mutation=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = """
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
    """ % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


def rem_en(input_txt):
    words = input_txt.lower().split()
    noise_free_words = [word for word in words if word not in stop] 
    noise_free_text = " ".join(noise_free_words) 
    return noise_free_text

def punctuation_removal(text):
    all_list = [char for char in text if char not in string.punctuation]
    clean_str = ''.join(all_list)
    return clean_str

stemmer = nltk.PorterStemmer()
def clean_text(text):
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    text = ' '.join([word for word in text.split() if word not in (stop)])#stopwords
    text =' '.join(re.sub("(w+://S+)", " ", text).split())#url
    text = rem_en(text)
    tokens = re.split('\W+', text)
    text = punctuation_removal(text)
    text = ''.join([i for i in text if not i.isdigit()])
    text = text.lower()
    text = text.split()
    text = [stemmer.stem(word) for word in text if not word in stopwords.words('english')]
    text = ' '.join(text)
    #text = [stemmer.stem(word) for word in tokens if word not in stopwords]
    return text

# Title
def main():
    set_bg('background.png')
    from PIL import Image
   # image = Image.open(model_file + "\logo.jpg")
  #  st.image(image)

    st.header("Hi,Welcome, to our Streamlit Fakenews classifier")
    st.write('Please Enter News text to check if it is fake news or not')
    activity = ['Prediction','NLP']
    choice = st.sidebar.selectbox("Select Activity",activity)
    if choice == 'Prediction' :
	    st.info("You have selected Prediction using ML algorithms")
    else :
      st.info("You have selected Prediction using NLP algorithms")

    news_text = st.text_area(" Enter News Below ","Enter Text Here...")
    all_ml_models = ["LOG_REG","RANDOM_FOREST","DECISION_TREE","GRADIENT_BOOST"]
    model_choice = st.selectbox("Select Model",all_ml_models)

    prediction_labels = {'business': 0,'tech': 1,'sport': 2,'health': 3,'politics': 4,'entertainment': 5}
    if st.button("Classify"):
       # st.text("Original Text is as below :\n{}".format(news_text))
        input_data_reshaped1 = clean_text(news_text)
        st.write("Input Text after Text processing : \n ", input_data_reshaped1)
        input_data_reshaped1 = [input_data_reshaped1]
        #vect_text = news_cv.transform([news_text]).toarray()
       # st.write(vect_text)
        if model_choice == 'LOG_REG':
            loaded_model = pickle.load(open('models\\model_LR.sav', 'rb'))
            prediction = loaded_model.predict(input_data_reshaped1)
            st.write('model_LR Prediction score is : ', prediction[0])
            if (prediction[0] == 0):
              st.markdown('<p style="font-family:sans-serif; color:Green; font-size: 48px;">The news is not fake!</p>', unsafe_allow_html=True)
            else:
              new_title = '<p style="font-family:sans-serif; color:Red; font-size: 48px;">The news is fake!</p>'
              st.markdown(new_title, unsafe_allow_html=True)
        elif model_choice == 'DECISION_TREE':
            loaded_model = pickle.load(open('models\\model_DTC.sav', 'rb'))
            prediction = loaded_model.predict(input_data_reshaped1)
            st.write('model_LR Prediction score is : ', prediction[0])
            if (prediction[0] == 0):
              st.markdown('<p style="font-family:sans-serif; color:Green; font-size: 48px;">The news is not fake!</p>', unsafe_allow_html=True)
            else:
              new_title = '<p style="font-family:sans-serif; color:Red; font-size: 48px;">The news is fake!</p>'
              st.markdown(new_title, unsafe_allow_html=True)
        elif model_choice == 'GRADIENT_BOOST':
            loaded_model = pickle.load(open('models\\model_LR.sav', 'rb'))
            prediction = loaded_model.predict(input_data_reshaped1)
            st.write('model_LR Prediction score is : ', prediction[0])
            if (prediction[0] == 0):
              st.markdown('<p style="font-family:sans-serif; color:Green; font-size: 48px;">The news is not fake!</p>', unsafe_allow_html=True)
            else:
              new_title = '<p style="font-family:sans-serif; color:Red; font-size: 48px;">The news is fake!</p>'
              st.markdown(new_title, unsafe_allow_html=True)
        elif model_choice == 'RANDOM_FOREST':
            loaded_model = pickle.load(open('models\\model_RFC.sav', 'rb'))
            prediction = loaded_model.predict(input_data_reshaped1)
            #st.write(prediction)
            st.write('model_LR Prediction score is : ', prediction[0])
            if (prediction[0] == 0):
              st.markdown('<p style="font-family:sans-serif; color:Green; font-size: 48px;">The news is not fake!</p>', unsafe_allow_html=True)
            else:
              new_title = '<p style="font-family:sans-serif; color:Red; font-size: 48px;">The news is fake!</p>'
              st.markdown(new_title, unsafe_allow_html=True)
        else :
            st.write('Choose any models')
            



if __name__ == '__main__':
	main()
