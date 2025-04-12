from pyexpat import features

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB ## MultinomialNB use to classify data
import streamlit as st

data = pd.read_csv("spam.csv")


##prints first 5 lines of the data set
##print(data.head(5))

#print data details
#print(data.shape)

#clean the data
data.drop_duplicates(inplace=True) ## inplace indicates, performing ops directly on datasets

#after cleaning
#print(data.shape)

#check for any null values
##print(data.isnull().sum())

##prints first 5 lines of the data set
#print(data.head(5))

#Replace ham and spam in category to 'not spam and Spam'
data['Category'] = data['Category'].replace(['ham','spam'],['Not Spam', 'Spam'])

#print after replacement
#print(data.head(5))

#Spliting the data sets in train data and test data
mess = data['Message']
cat = data['Category']

(mess_train,mess_test,cat_train,cat_test) = train_test_split(mess, cat, test_size=0.2)

#Convert text data in to numerical format using the CountVectorizer Algorithm

cv = CountVectorizer(stop_words='english') ##eleminating common english word
features = cv.fit_transform(mess_train)

#Creating the Model
model = MultinomialNB()
model.fit(features, cat_train)

#Test our model
features_test = cv.transform(mess_test)
##print(model.score(features_test, cat_test))

#predict the data
#message = cv.transform(['Congratulations, you won a lottery']).toarray()
#result = model.predict(message)
#print(result)

#Convert it to a function
def predict(message):
    input_message = cv.transform([message]).toarray()
    result = model.predict(input_message)
    return result

st.header('Spam Detector')

input_mess = st.text_input('Enter Message Here')

if st.button('Validate'):
    output = predict(input_mess)
    st.markdown(output)


###for running streamlit
# streamlit run spam-detect-web.py

