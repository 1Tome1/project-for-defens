from sklearn.neural_network import MLPClassifier
import numpy as np
import sklearn as sk
import pickle


survey = np.array([
 [54, 165, 1],
 [65, 183, 0],
 [62, 178, 0],
 [49, 152, 1],
 [48, 156, 1],
 [72, 192, 0],
 [55, 162, 1],
 [94, 172, 0],
 [40, 142, 1],
 [53, 157, 1],
 [80, 180, 0],
 [85, 184, 0],
 ])

features_train = survey[:, 0:2]
labels_train = survey[:, 2]

mlp = MLPClassifier(hidden_layer_sizes=(10),
	max_iter=100000, # epochs
)

mlp.fit(features_train, labels_train)

features_test = ([[52, 163]])
labels_test = ([[1]])


print(f"Training set score: {mlp.score(features_train, labels_train):.3%}")
print(f"Testing set score: {mlp.score(features_test, labels_test):.3%}\n")


while True:
    h=int(input("Введите 1 если хотите выйти и 2 если хотите сохранить нейросеть"))
    if h == 1:
        break
    elif h == 2:
        pkl_filename = "pickle_model.pkl" 
        with open(pkl_filename, 'wb') as file: 
            pickle.dump(mlp, file)

    x = int(input("Введите вес"))
    y = int(input("Введите рост"))


    test = ([[x, y]])

    if (mlp.predict(test) == 1):
        print("Женщина")
    else:
        print("Мужчина")