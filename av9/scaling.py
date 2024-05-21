from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler

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

    standard_scaler = StandardScaler()
    standard_scaler.fit(train_X)
    minmax_scaler = MinMaxScaler()
    minmax_scaler.fit(train_X)


    classifier = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier.fit(train_X, train_Y)
    classifier2.fit(standard_scaler.transform(train_X), train_Y)
    classifier3.fit(minmax_scaler.transform(train_X), train_Y)

    accuracy = 0
    predictions = classifier.predict(val_X)

    for true, prediction in zip(val_Y, predictions):
        if true == prediction:
            accuracy += 1

    accuracy = accuracy / len(val_Y)

    print(f'Bez normalizacija: {accuracy}')

    accuracy = 0
    predictions = classifier2.predict(standard_scaler.transform(val_X))

    for true, prediction in zip(val_Y, predictions):
        if true == prediction:
            accuracy += 1

    accuracy = accuracy / len(val_Y)

    print(f'Standardna normalizacija: {accuracy}')

    accuracy = 0
    predictions = classifier3.predict(minmax_scaler.transform(val_X))

    for true, prediction in zip(val_Y, predictions):
        if true == prediction:
            accuracy += 1

    accuracy = accuracy / len(val_Y)

    print(f'Minmax normalizacija: {accuracy}')

    tp, fp, tn, fn = 0, 0, 0, 0
    predictions = classifier3.predict(minmax_scaler.transform(test_X))
    for true, prediction in zip(test_Y, predictions):
        if true == 'good':
            if true == prediction:
                tp += 1
            else:
                fn += 1
        else:
            if true == prediction:
                tn += 1
            else:
                fp += 1

    accuracy = (tp + tn) / (tp + fp + tn + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    print("Evaluacija:")
    print(f'Tochnost: {accuracy}')
    print(f'Preciznost: {precision}')
    print(f'Odziv: {recall}')



