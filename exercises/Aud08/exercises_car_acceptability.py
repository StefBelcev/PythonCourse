import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    with open("car.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]

        encoder = OrdinalEncoder()
        encoder.fit([row[:-1] for row in dataset])

        train_set = dataset[:int(0.7 * len(dataset))]
        features_training_set = [t[:-1] for t in train_set]
        features_training_set = encoder.transform(features_training_set)
        class_training_set = [t[-1] for t in train_set]

        test_set = dataset[int(0.7 * len(dataset)):]
        features_test_set = [t[:-1] for t in test_set]
        features_test_set = encoder.transform(features_test_set)
        class_test_set = [t[-1] for t in test_set]

        classifier = DecisionTreeClassifier(criterion='entropy')
        classifier.fit(features_training_set, class_training_set)

        depth_tree = classifier.get_depth()
        number_leaves = classifier.get_n_leaves()

        print(f'Depth:{depth_tree}')
        print(f'Number of leaves:{number_leaves}')

        accuracy = 0
        for x, y in zip(features_test_set, class_test_set):
            y_predicted = classifier.predict([x])[0]
            if y_predicted == y:
                accuracy += 1
        percentage = accuracy / len(test_set)
        print(percentage)

        feature_importances = list(classifier.feature_importances_)
        most_important_feature = feature_importances.index(max(feature_importances))
        least_important_feature = feature_importances.index(min(feature_importances))

        print(f'Feature importances: {feature_importances}')
        print(f'Most important feature: {most_important_feature}')
        print(f'Least important feature: {least_important_feature}')

        # train_x_5 = [[features_training_set[i][j] for j in range(len(features_training_set[i])) if j != 5]
        #              for i in range(len(features_training_set))]
        #
        train_x_5 = list()
        for t in features_training_set:
            sample = [t[i] for i in range(len(t)) if i != most_important_feature]
            train_x_5.append(sample)

        test_x_5 = list()
        for t in features_test_set:
            sample = [t[i] for i in range(len(t)) if i != most_important_feature]
            test_x_5.append(sample)

        clf5 = DecisionTreeClassifier(criterion='entropy')
        clf5.fit(train_x_5, class_training_set)

        accuracy5 = 0
        for x, y in zip(test_x_5, class_test_set):
            y_predicted = clf5.predict([x])[0]
            if y_predicted == y:
                accuracy5 += 1
        percentage5 = accuracy5 / len(test_set)
        # print(percentage5)
        print(f'Depth (removed most important feature) : {clf5.get_depth()}')
        print(f'Number of leaves (removed most important feature) : {clf5.get_n_leaves()}')
        print(f'Accuracy for the model without the most important feature: {percentage5}')

        # train_x_2 = [[features_training_set[i][j] for j in range(len(features_training_set[i])) if j != 2]
        #              for i in range(len(features_training_set))]

        train_x_2 = list()
        for t in features_training_set:
            sample = [t[i] for i in range(len(t)) if i != least_important_feature]
            train_x_2.append(sample)

        test_x_2 = list()
        for t in features_test_set:
            sample = [t[i] for i in range(len(t)) if i != least_important_feature]
            test_x_2.append(sample)

        clf2 = DecisionTreeClassifier(criterion='entropy')
        clf2.fit(train_x_2, class_training_set)

        accuracy2 = 0
        for x, y in zip(test_x_2, class_test_set):
            y_predicted = clf2.predict([x])[0]
            if y_predicted == y:
                accuracy2 += 1
        percentage2 = accuracy2 / len(test_set)

        print(f'Depth (removed least important feature) : {clf2.get_depth()}')
        print(f'Number of leaves (removed least important feature) : {clf2.get_n_leaves()}')
        print(f'Accuracy for the model without the least important feature: {percentage2}')
