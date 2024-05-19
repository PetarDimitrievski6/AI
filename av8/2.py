import csv

from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]

    return dataset


if __name__ == '__main__':
    dataset = read_file('car.csv')
    encoder = OrdinalEncoder()

    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(len(dataset) * 0.7)]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[int(len(dataset) * 0.7):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)
    classifier.fit(train_x, train_y)

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)

    print(f"Accuracy: {accuracy}")

    feature_importances = list(classifier.feature_importances_)
    print(f'Feature importances: {feature_importances}')

    most_important_feature = feature_importances.index(max(feature_importances))
    print(f'Most important feature: {most_important_feature}')
    least_important_feature = feature_importances.index(min(feature_importances))
    print(f'Least important feature: {least_important_feature}')



