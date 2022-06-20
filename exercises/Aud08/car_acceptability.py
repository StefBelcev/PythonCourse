import csv
import math
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

def divide_dataset(dataset):
    train_set = dataset[:math.ceil(0.7 * len(dataset))]
    test_set = dataset[math.ceil(0.7 * len(dataset)):]
    return train_set, test_set


if __name__ == '__main__':
    with open("car.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]

        encoder = OrdinalEncoder()
        encoder.fit([dataset[i][:-1] for i in range(len(dataset))])

        train_set, test_set = divide_dataset(dataset)
        x_train_set = [train_set[i][:-1] for i in range(len(train_set))]
        x_train_set = encoder.transform(x_train_set)
        y_train_set = [train_set[i][-1] for i in range(len(train_set))]