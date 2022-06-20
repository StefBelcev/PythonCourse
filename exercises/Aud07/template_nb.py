import csv
import math
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import CategoricalNB


def divide_sets(dataset):
    train_set = dataset[0: math.ceil(0.75 * len(dataset))]
    test_set = dataset[math.ceil(0.75 * len(dataset)):]
    return train_set, test_set


def divide_characteristics(train_set):
    x = [train_set[i][:-1] for i in range(len(train_set))]
    y = [train_set[i][-1] for i in range(len(train_set))]
    return x, y


def model_accuracy(test_set):
    accuracy = 0
    for i in range(len(test_set)):
        predict = clf.predict([test_set[i][:-1]])
        if predict[0] == test_set[i][-1]:
            accuracy += 1
    percentage = accuracy/len(test_set)
    return percentage


def model_accuracy_categorical(test_set, test_set_x):
    accuracy = 0
    for i in range(len(test_set)):
        predict = clf.predict([test_set_x[i]])
        if predict[0] == test_set[i][-1]:
            accuracy += 1
    percetange = accuracy/len(test_set)
    return percetange


if __name__ == '__main__':
    with open("categorical_naive_bayes/car.csv") as csv_cars:
        cvs_reader_cars = csv.reader(csv_cars, delimiter=',')
        dataset_cars = list(cvs_reader_cars)[1:]
        encoder = OrdinalEncoder()
        encoder.fit([dataset_cars[i][:-1] for i in range(len(dataset_cars))])

        train_set_cars, test_set_cars = divide_sets(dataset_cars)

        x_train, y_train = divide_characteristics(train_set_cars)
        x_train = encoder.transform(x_train)

        clf = CategoricalNB()
        clf.fit(x_train, y_train)

        test_set_cars_x = [test_set_cars[i][-1] for i in range(len(test_set_cars))]
        test_set_cars_x = encoder.transform(test_set_cars_x)

        percentage_cars = model_accuracy_categorical(test_set_cars, test_set_cars_x)

    with open("gaussian_naive_bayes/medical_data.csv") as csv_diabetis:
        cvs_reader_diabetis = csv.reader(csv_diabetis, delimiter=',')
        dataset_diabetis = list(cvs_reader_diabetis)[1:]
        dataset_diabetis = [[int(dataset_diabetis[i][j]) for j in range(len(dataset_diabetis[i]))]
                            for i in range(len(dataset_diabetis))]
        train_set_diabetis, test_set_diabetis = divide_sets(dataset_diabetis)
        x_train, y_train = divide_sets(dataset_diabetis)

        clf = GaussianNB()
        clf.fit(x_train, y_train)

        percentage_diabetis = model_accuracy(test_set_diabetis)

