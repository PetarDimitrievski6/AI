from zad2_dataset import dataset
from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':
    dataset = [[float(e) for e in row] for row in dataset]

    train_set = dataset[:int(len(dataset) * 0.85)]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(len(dataset) * 0.85):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy += 1

    print(accuracy / len(test_set))

    entry = [float(e) for e in input().split(' ')]
    entry_class = classifier.predict([entry])[0]
    print(int(entry_class))
    print(classifier.predict_proba([entry]))

