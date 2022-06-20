import math
import csv
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OrdinalEncoder


def divide_dataset(dataset):
    train_set = dataset[0: math.ceil(0.8 * len(dataset))]
    test_set = dataset[math.ceil(0.8 * len(dataset)):]
    return train_set, test_set


def divide_characteristics(train_set):
    X = [train_set[i][:-1] for i in range(len(train_set))]
    Y = [train_set[i][-1] for i in range(len(train_set))]
    return X, Y


def model_accuracy(test_set):
    accuracy = 0
    for i in range(len(test_set)):
        predicted_class = clf.predict([test_set[i][:-1]])
        if predicted_class[0] == test_set[i][-1]:
            accuracy += 1
    return accuracy / len(test_set)


if __name__ == '__main__':

    with open("medical_data.csv") as csv_file:
        cvs_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(cvs_reader)[1:]
        # print(dataset)
        dataset = [[int(dataset[i][j]) for j in range(len(dataset[i]))] for i in range(len(dataset))]
        # print(dataset)
        train_set, test_set = divide_dataset(dataset)
        x_train, y_train = divide_characteristics(train_set)
        clf = GaussianNB()
        clf.fit(x_train, y_train)

        test_set_x = [test_set[i][:-1] for i in range(len(test_set))]

        print(clf.predict([test_set[0][:-1]]))
        print(clf.predict_proba([test_set[0][:-1]]))
        # prv nacin
        accuracy = 0
        for row in test_set:
            prediction = clf.predict([row[:-1]])
            if prediction[0] == row[-1]:
                accuracy += 1
        print(accuracy/len(test_set))
        # vtor nacin
        accuracy1 = 0
        for i in range(len(test_set)):
            predict = clf.predict([test_set_x[i]])
            if predict[0] == test_set[i][-1]:
                accuracy1 += 1
        print(accuracy1/len(test_set))

        print(model_accuracy(test_set))
        # entry = [int(el) for el in input().split(" ")]
        # predict = clf.predict([entry])
        # print(predict)
        # predict_proba = clf.predict_proba([entry])
        # print(predict_proba)
