import pickle
import numpy as np
import file

print("Running bugs prediction...")
print(" ")

# GET THE DATA FROM file.py
data = file.getattributes()

with open('/home/ramith/PycharmProjects/FYP/model_pickle', 'rb') as f:
    mp = pickle.load(f)

example_measures = np.array(data)
example_measures = example_measures.reshape(1, -1)
prediction = mp.predict(example_measures)

print(data)

if prediction == 1:
    print("Code might contains bugs")
else:
    print("Code does not contain any bugs")