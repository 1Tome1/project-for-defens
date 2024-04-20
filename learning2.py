from sklearn.neural_network import MLPClassifier
import numpy as np
import sklearn as sk
import pickle


pkl_filename = "pickle_model.pkl"

with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)


features_test = ([[49, 150]])
labels_test = ([[1]])

print(f"Testing set score: {pickle_model.score(features_test, labels_test):.3%}\n")

while True:
    h=int(input("Введите 1 если хотите выйти"))
    if h == 1:
        break
    

    x = int(input("Введите вес"))
    y = int(input("Введите рост"))


    test = ([[x, y]])

    if (pickle_model.predict(test) == 1):
        print("Женщина")
    else:
        print("Мужчина")