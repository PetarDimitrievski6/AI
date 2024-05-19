import csv

from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier


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

    # classifier = DecisionTreeClassifier(criterion='entropy', max_depth=5, max_leaf_nodes=20, random_state=0)
    classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier.fit(train_x, train_y)

    print(f'Depth: {classifier.get_depth()}')
    print(f'Leaves: {classifier.get_n_leaves()}')

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

    train_x_2 = [[t[i] for i in range(len(t)) if i != most_important_feature] for t in train_x]
    test_x_2 = [[t[i] for i in range(len(t)) if i != most_important_feature] for t in test_x]

    train_x_3 = [[t[i] for i in range(len(t)) if i != least_important_feature] for t in train_x]
    test_x_3 = [[t[i] for i in range(len(t)) if i != least_important_feature] for t in test_x]

    classifier2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier2.fit(train_x_2, train_y)

    classifier3 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier3.fit(train_x_3, train_y)

    print(f'Depth (without most important feature): {classifier2.get_depth()}')
    print(f'Leaves (without most important feature): {classifier2.get_n_leaves()}')

    print(f'Depth (without least important feature): {classifier3.get_depth()}')
    print(f'Leaves (without least important feature): {classifier3.get_n_leaves()}')

    accuracy2 = 0

    for i in range(len(test_set)):
        predicted_class = classifier2.predict([test_x_2[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy2 += 1

    accuracy2 = accuracy2 / len(test_set)

    print(f"Accuracy (without most important feature): {accuracy2}")

    accuracy3 = 0

    for i in range(len(test_set)):
        predicted_class = classifier3.predict([test_x_3[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy3 += 1

    accuracy3 = accuracy3 / len(test_set)

    print(f"Accuracy (without least important feature): {accuracy3}")


