import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

df = pd.read_csv("data.csv")
#df.replace('true', 1, inplace=True)
#df.replace('false', 0, inplace=True)
#df.drop([], 1, inplace=True)
#print(df)

X = np.array(df.drop(['CLASS'], 1))
y = np.array(df['CLASS'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = RandomForestClassifier(n_estimators=20)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures = np.array([11,9,2,3,13,85,9,250])
example_measures = example_measures.reshape(1, -1)
prediction = clf.predict(example_measures)
#if prediction == 1:
#    print(prediction)
#    print("Code contains bugs")
#else:
#    print(prediction)
 #   print("Code does not contain any bugs")

with open('model_pickle', 'wb') as f:
    pickle.dump(clf, f)