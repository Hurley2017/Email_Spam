import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


raw_mail_data = pd.read_csv('mail_data.csv')
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)), '')

mail_data.loc[mail_data['Category'] == "spam", "Category",] = 0
mail_data.loc[mail_data['Category'] == "ham", "Category",] = 1

X = mail_data["Message"]
Y = mail_data["Category"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase=True)
X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

Model = LogisticRegression()

Model.fit(X_train_features, Y_train)

prediction_on_training_data = Model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)

prediction_on_test_data = Model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)

def retCheck(message):
  Choice_Dict = {1:"Not Spam", 0:"Spam"}
  input_email = [message]
  Numeric_Equivalence = feature_extraction.transform(input_email)
  predicted = Model.predict(Numeric_Equivalence)
  return Choice_Dict[int(predicted)]
