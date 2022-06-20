import csv
import math
from sklearn.naive_bayes import GaussianNB
if __name__ == '__main__':
    with open("medical_data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        dataset = list(csv_reader)[1:]
        dataset = [[int(dataset[i][j]) for j in range(len(dataset[i]))] for i in range(len(dataset))]

        train_set = dataset[0:math.ceil(0.8 * len(dataset))]
        test_set = dataset[math.ceil(0.8 * len(dataset)):]

        X = [train_set[i][:-1] for i in range(len(train_set))]
        Y = [train_set[i][-1] for i in range(len(train_set))]

        clf = GaussianNB()
        clf.fit(X, Y)

        print(clf.predict([test_set[0][:-1]]))
        print(clf.predict_proba([test_set[0][:-1]]))

        # entry = [int(el) for el in input().split(" ")]
        # print(clf.predict_proba([entry]))

        accuracy = 0
        for row in test_set:
            predict = clf.predict([row[:-1]])
            if predict[0] == row[-1]:
                accuracy += 1
        print(accuracy/len(test_set))
