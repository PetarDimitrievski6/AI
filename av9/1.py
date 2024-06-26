from sklearn.neural_network import MLPClassifier


def read_dataset():
    data = []
    with open('winequality.csv') as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == "":
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

    train_X = [x[:-1] for x in train_set]
    train_Y = [x[-1] for x in train_set]
    val_X = [x[:-1] for x in val_set]
    val_Y = [x[-1] for x in val_set]
    test_X = [x[:-1] for x in test_set]
    test_Y = [x[-1] for x in test_set]

    classifier = MLPClassifier(5, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(100, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier.fit(train_X, train_Y)
    classifier2.fit(train_X, train_Y)
    classifier3.fit(train_X, train_Y)


    final_classifier = None
    max_accuracy = 0

    for i,c in enumerate([classifier, classifier2, classifier3]):
        val_predictions = c.predict(val_X)
        accuracy = 0
        for true, prediction in zip(val_Y, val_predictions):
            if true == prediction:
                accuracy += 1

        accuracy = accuracy / len(val_Y)

        print(f'Classifier {i} accuracy: {accuracy}')

        if accuracy > max_accuracy:
            max_accuracy = accuracy
            final_classifier = c

    accuracy = 0
    predictions = final_classifier.predict(test_X)

    for true, prediction in zip(test_Y, predictions):
        if true == prediction:
            accuracy += 1

    accuracy = accuracy / len(test_Y)

    print(f'Test accuracy: {accuracy}')


