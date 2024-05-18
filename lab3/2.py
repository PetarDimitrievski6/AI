import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
# Vashiot kod tuka
    train_set = dataset[:int(len(dataset) * 0.85)]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_set = dataset[int(len(dataset) * 0.85):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_X, train_Y)

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_X[i]])[0]
        true_class = test_Y[i]

        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)

    print(accuracy)

    entry = [float(e) for e in input().split(" ")]

    predicted_class = classifier.predict([entry])[0]

    print(predicted_class)

    print(classifier.predict_proba([entry]))

# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

# submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

# submit na klasifikatorot
    submit_classifier(classifier)

# povtoren import na kraj / ne ja otstranuvajte ovaa linija
