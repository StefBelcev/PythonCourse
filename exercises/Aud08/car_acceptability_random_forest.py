import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier


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

        classifier = RandomForestClassifier(random_state=0, n_estimators=5, criterion='entropy')
        classifier.fit(features_training_set, class_training_set)

        correct_samples = 0
        for x, y in zip(features_test_set, class_test_set):
            y_predicted = classifier.predict([x])[0]
            if y_predicted == y:
                correct_samples += 1
        accuracy = correct_samples/len(test_set)
        print(f'Accuracy of the Random Tree Classifier with 3 trees is: {accuracy}')
        feature_importances = list(classifier.feature_importances_)
        most_important_feature = feature_importances.index(max(feature_importances))
        least_important_feature = feature_importances.index(min(feature_importances))
        print(f'Most important feature is {most_important_feature + 1}')
        print(f'Least important feature is {least_important_feature + 1}')