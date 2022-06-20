import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import CategoricalNB
from sklearn.neural_network import MLPClassifier

dataset = [[0.223, 0.226, 0.889, 0.267, 0.276, 0.689, 0.253, 0.426, 0.883, 1],
           [0.554, 0.446, 0.598, 0.299, 0.246, 0.699, 0.753, 0.476, 0.843, 0],
           [0.667, 0.567, 0.432, 0.255, 0.256, 0.659, 0.753, 0.456, 0.853, 1],
           [0.237, 0.566, 0.777, 0.298, 0.288, 0.689, 0.793, 0.468, 0.863, 0],
           [0.223, 0.226, 0.889, 0.290, 0.206, 0.609, 0.783, 0.426, 0.843, 1],
           [0.554, 0.446, 0.556, 0.232, 0.246, 0.559, 0.798, 0.457, 0.859, 0],
           [0.667, 0.567, 0.432, 0.245, 0.256, 0.644, 0.711, 0.896, 0.243, 1],
           [0.634, 0.127, 0.499, 0.232, 0.246, 0.559, 0.798, 0.457, 0.859, 0],
           [0.237, 0.566, 0.777, 0.255, 0.256, 0.659, 0.753, 0.456, 0.853, 0],
           [0.223, 0.226, 0.889, 0.889, 0.267, 0.276, 0.689, 0.253, 0.426, 1],
           [0.554, 0.446, 0.556, 0.226, 0.889, 0.290, 0.206, 0.609, 0.783, 0],
           [0.667, 0.567, 0.432, 0.223, 0.226, 0.889, 0.290, 0.206, 0.609, 1],
           [0.634, 0.127, 0.499, 0.255, 0.256, 0.659, 0.753, 0.456, 0.853, 0],
           [0.237, 0.566, 0.777, 0.123, 0.126, 0.189, 0.190, 0.206, 0.699, 0]]

if __name__ == '__main__':
    encoder = OrdinalEncoder()  # za da gi pretvori vo integer array
    X = int(input())

    train_set = dataset[:X]  # ako e prvite 7 samo ova train_set = dataset[:7]
    # train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [t[:-1] for t in train_set]  # prv del bez klasa go deli mnozestvoto
    # print(train_x)
    train_x = encoder.fit_transform(train_x)
    train_y = [t[-1] for t in train_set]  # klasa (1 ili 0)

    test_set = dataset[X:]
    # test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [t[:-1] for t in test_set]
    test_x = encoder.fit_transform(test_x)
    test_y = [t[-1] for t in test_set]

    tip = input()  # DT, NB ili NN kako string
    indeksKolona = int(input())

    # bez kolona datasetot
    newDataSet = [row[:indeksKolona] + row[indeksKolona + 1:] for row in dataset]

    train_set_bezKolona = newDataSet[:X]  # ako e prvite 7 samo ova train_set = dataset[:7]
    # train_set = dataset[:int(0.7 * len(dataset))]
    train_x_bezKolona = [t[:-1] for t in train_set_bezKolona]  # prv del bez klasa go deli mnozestvoto
    train_x_bezKolona = encoder.fit_transform(train_x_bezKolona)
    train_y_bezKolona = [t[-1] for t in train_set_bezKolona]  # klasa (1.0)

    test_set_bezKolona = newDataSet[X:]
    # test_set = dataset[int(0.7 * len(dataset)):]
    test_x_bezKolona = [t[:-1] for t in test_set_bezKolona]
    test_x_bezKolona = encoder.fit_transform(test_x_bezKolona)
    test_y_bezKolona = [t[-1] for t in test_set_bezKolona]

    if tip == 'DT':

        classifier_1 = DecisionTreeClassifier(criterion='entropy')  # deklariram klasifikator
        classifier_1.fit(train_x, train_y)  # sekogas fit

        # print(f'Depth: {classifier.get_depth()}')
        # print(f'Number of leaves: {classifier.get_n_leaves()}')

        correct_samples1 = 0
        for x, y in zip(test_x, test_y):
            y_predicted = classifier_1.predict([x])[0]  # ja vrakja prvata klasa sto ja predviduva
            if y == y_predicted:  # y mi e tocnata klasa sporeduva so predvidenata
                correct_samples1 += 1

        accuracy1 = correct_samples1 / len(test_set)  # za preciznost
        # print(f'Accuracy: {accuracy1}')

        classifier_2 = DecisionTreeClassifier(criterion='entropy')  # deklariram klasifikator
        classifier_2.fit(train_x_bezKolona, train_y_bezKolona)  # sekogas fit

        # print(f'Depth: {classifier.get_depth()}')
        # print(f'Number of leaves: {classifier.get_n_leaves()}')

        correct_samples2 = 0
        for x, y in zip(test_x_bezKolona, test_y_bezKolona):
            y_predicted = classifier_2.predict([x])[0]  # ja vrakja prvata klasa sto ja predviduva
            if y == y_predicted:  # y mi e tocnata klasa sporeduva so predvidenata
                correct_samples2 += 1

        accuracy2 = correct_samples2 / len(test_set_bezKolona)  # za preciznost
        # print(f'Accuracy: {accuracy2}')

        if (accuracy1 > accuracy2):
            print('Klasifikatorot so site koloni ima pogolema tocnost')
            print(accuracy1)

        elif (accuracy1 < accuracy2):
            print('Klasifikatorot so edna kolona pomalku ima pogolema tocnost')
            print(accuracy2)

        else:
            print('Klasifikatorite imaat ista tocnost')
            print(accuracy1)  # bilo koj

    elif tip == 'NB':
        classifier_NB = CategoricalNB()
        classifier_NB.fit(train_x, train_y)  # koga imam fit train, dovolno e ednas da treniram

        # test_set_x = encoder.transform([test_set[i][:-1] for i in range(0, len(test_set))]) ja zema samo klasata od sekoja redica
        accuracy = 0
        for i in range(0, len(test_set)):  # moze da bide i test_x
            predict = classifier_NB.predict([test_x[i]])  # so predict sekogas testiram, testiram kolku sakam
            # if predict[0] == test_set[i][-1]:
            if predict[0] == test_y[i]:
                # correct_test
                accuracy += 1

        # print(accuracy / len(test_set))
        c1 = accuracy / len(test_set)
        # klasifikator bez kolonata
        classifier_NB_2 = CategoricalNB()
        classifier_NB_2.fit(train_x_bezKolona, train_y_bezKolona)  # koga imam fit train, dovolno e ednas da treniram

        # test_set_x = encoder.transform([test_set[i][:-1] for i in range(0, len(test_set))]) ja zema samo klasata od sekoja redica
        accuracy1 = 0
        for i in range(0, len(test_x_bezKolona)):  # moze da bide i test_x
            predict = classifier_NB.predict([test_x_bezKolona[i]])  # so predict sekogas testiram, testiram kolku sakam
            # if predict[0] == test_set[i][-1]:
            if predict[0] == test_y_bezKolona[i]:
                # correct_test
                accuracy1 += 1

        # print(accuracy1 / len(test_set))
        c2 = accuracy1 / len(test_set)
        # entry = [el for el in input().split(' ')] #da gi vnesam kako redica(string) atributite
        # entry = encoder.transform([entry])
        # print(clf.predict(entry)) #printa predvidena klasa

        if (c1 > c2):
            print('Klasifikatorot so site koloni ima pogolema tocnost')
            print(c1)

        elif (c1 < c2):
            print('Klasifikatorot so edna kolona pomalku ima pogolema tocnost')
            print(c2)

        else:
            print('Klasifikatorite imaat ista tocnost')
            print(c2)  # bilo koj
    elif tip == 'NN':
        classifier_NN = MLPClassifier(3, activation='relu', learning_rate_init=0.003, max_iter=200, random_state=0)
        classifier_NN_2 = MLPClassifier(3, activation='relu', learning_rate_init=0.003, max_iter=200, random_state=0)

        classifier_NN.fit(train_x, train_y)
        classifier_NN_2.fit(train_x_bezKolona, train_y_bezKolona)

        acc1 = 0
        predictions = classifier_NN.predict(test_x)
        for true, pred in zip(test_y, predictions):
            if true == pred:
                acc1 += 1

        acc1 = acc1 / len(test_y)

        correct = 0
        predictions = classifier_NN.predict(test_x_bezKolona)
        for true, pred in zip(test_y_bezKolona, predictions):
            if true == pred:
                correct += 1

        correct = correct / len(test_y_bezKolona)

        # sporedba koj klasifikator e podobar dali bez kolona ili so

        if acc1 > correct:
            print('Klasifikatorot so site koloni ima pogolema tocnost')
            print(acc1)

        elif acc1 < correct:
            print('Klasifikatorot so edna kolona pomalku ima pogolema tocnost')
            print(correct)

        else:
            print('Klasifikatorite imaat ista tocnost')
            print(correct)  # bilo koj
