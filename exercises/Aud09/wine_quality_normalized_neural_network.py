import csv
import math
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def read_dataset():
    data = []
    with open('winequality.csv') as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(';')
            data.append(list(map(float, parts[:-1])) + parts[-1:])

    return data


def divide_sets(dataset):
    bad_classes = [x for x in dataset if x[-1] == 'bad']
    good_classes = [x for x in dataset if x[-1] == 'good']


    train_set = bad_classes[:int(len(bad_classes) * 0.7)] + good_classes[:int(len(good_classes) * 0.7)]
    val_set = bad_classes[int(len(bad_classes) * 0.7):int(len(bad_classes) * 0.8)] + \
              good_classes[int(len(good_classes) * 0.7):int(len(good_classes) * 0.8)]
    test_set = bad_classes[int(len(bad_classes) * 0.8):] + good_classes[int(len(good_classes) * 0.8):]

    return train_set, val_set, test_set


if __name__ == '__main__':
    dataset = read_dataset()
    train_set, val_set, test_set = divide_sets(dataset)

    train_x = [x[:-1] for x in train_set]
    train_y = [x[-1] for x in train_set]
    val_x = [x[:-1] for x in val_set]
    val_y = [x[-1] for x in val_set]
    test_x = [x[:-1] for x in test_set]
    test_y = [x[-1] for x in test_set]

    classifier = MLPClassifier(10, activation='relu', max_iter=500, learning_rate_init=0.001, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', max_iter=500, learning_rate_init=0.001, random_state=0)
    classifier3= MLPClassifier(10, activation='relu', max_iter=500, learning_rate_init=0.001, random_state=0)

    min_max_scaler = MinMaxScaler()
    min_max_scaler.fit(train_x)

    standard_scaler = StandardScaler()
    standard_scaler.fit(train_x)


    classifier.fit(train_x, train_y)
    classifier2.fit(min_max_scaler.transform(train_x), train_y)
    classifier3.fit(standard_scaler.transform(train_x), train_y)

    val_acc1 = 0
    val_predictions1 = classifier.predict(val_x)
    for true, prediction in zip(val_y, val_predictions1):
        if true == prediction:
            val_acc1 += 1
    val_acc1 = val_acc1 / len(val_y)

    val_acc2 = 0
    val_predictions2 = classifier2.predict(min_max_scaler.transform(val_x))

    for true, prediction in zip(val_y, val_predictions2):
        if true == prediction:
            val_acc2 += 1
    val_acc2 = val_acc2 / len(val_y)

    val_acc3 = 0
    val_predictions3 = classifier3.predict(standard_scaler.transform(val_x))

    for true, prediction in zip(val_y, val_predictions3):
        if true == prediction:
            val_acc3 += 1
    val_acc3 = val_acc3 / len(val_y)

    print(f'Bez normalizacija imame tocnost so validacisko mnozestvo od: {val_acc1}')
    print(f'So MinMaxScaler normalizacija imame tocnost so validacisko mnozestvo od: {val_acc2}')
    print(f'So Standard Scaler normalizacija imame tocnost so validacisko mnozestvo od: {val_acc2}')