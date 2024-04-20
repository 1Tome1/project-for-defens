from sklearn.neural_network import MLPClassifier
import numpy as np
import sklearn as sk
import pickle

import app


pkl_filename = "pickle_model.pkl"

with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)



def Start():
    x = app.label1.get()
    y = app.label2.get()

    test = ([[x, y]])
    app.textbox3.text = pickle_model.predict(test)


#pickle_model.predict(test)
        

