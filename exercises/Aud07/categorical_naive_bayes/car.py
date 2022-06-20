import csv
import math
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB


def separate_set(dataset):
    train_set = dataset[0: math.ceil(0.7 * len(dataset))]
    test_set = dataset[math.ceil(0.7 * len(dataset)):]
    return train_set, test_set


def divide_characteristics(dataset):
    X_train = [dataset[i][:-1] for i in range(len(dataset))]
    Y_train = [dataset[i][-1] for i in range(len(dataset))]
    return X_train, Y_train


def model_accuracy(dataset):
    accuracy = 0
    for row in dataset:
        predict = clf.predict([row[:-1]])
        if predict == row[-1]:
            accuracy += 1
    percentage = accuracy/(len(dataset))
    return percentage


if __name__ == '__main__':
    with open("car.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]
        encoder = OrdinalEncoder()
        encoder.fit([dataset[i][:-1] for i in range(len(dataset))])

        train_set = dataset[0: math.ceil(0.7 * len(dataset))]
        test_set = dataset[math.ceil(0.7 * len(dataset)):]

        X = [train_set[i][:-1] for i in range(0, len(train_set))]
        X = encoder.transform(X)
        Y = [train_set[i][-1] for i in range(0, len(train_set))]

        clf = CategoricalNB()
        clf.fit(X, Y)

        test_set_x = encoder.transform([test_set[i][:-1] for i in range(0, len(test_set))])

        accuracy = 0
        for i in range(0, len(test_set)):
            predict = clf.predict([test_set_x[i]])
            if predict[0] == test_set[i][-1]:
                accuracy += 1
        print(accuracy / len(test_set))

        entry = [el for el in input().split(' ')]
        entry = encoder.transform([entry])
        print(clf.predict(entry))

