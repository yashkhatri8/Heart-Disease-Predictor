import numpy as np
from pandas import read_csv
import pickle
data=read_csv("heart.csv")


data['thal']=data.thal.fillna(data.thal.mean())
data['ca']=data.thal.fillna(data.ca.mean())
x=data.iloc[:,:-1]
y=data.iloc[:,-1].values


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=0)


from sklearn.ensemble import RandomForestClassifier
classifier= RandomForestClassifier(n_estimators=10)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)

filename='heart-Disease-prediction.pkl'
pickle.dump(classifier,open(filename,'wb'))