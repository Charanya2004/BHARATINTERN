# -*- coding: utf-8 -*-
"""TASK2-TITANIC CLASSIFICATION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K22ogLq-NddQ9HFsbncEY8xdn4T8vIkI
"""

from google.colab  import drive
drive.mount('/content/drive')

import numpy as n
import pandas as p
import matplotlib.pyplot as plot
import seaborn as sb

file=p.read_csv("/content/drive/MyDrive/tested.csv")
file.head()

file.describe()

file['Survived'].value_counts()

sb.countplot(x=file['Survived'],hue=file['Embarked'])

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
file['Sex']=le.fit_transform(file['Sex'])
file.head()

sb.countplot(x=file['Sex'],hue=file['Survived'])

X=file[['Pclass','Sex']]
Y=file['Survived']

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.linear_model import LogisticRegression

l=LogisticRegression(random_state=0)
l.fit(X_train,Y_train)

prediction=print(l.predict(X_test))

print(Y_test)

#predict whether Survived or Not
#pred_result=l.predict[[Pclass,Sex]]
import warnings
warnings.filterwarnings("ignore")
pred_result=l.predict([[3,1]])
if(pred_result==0):
  print("Not Survived")
else:
  print("Survived")