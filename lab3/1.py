import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
# Vashiot kod tuka

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(len(dataset) * 0.75)]

    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    train_X = encoder.transform(train_X)

    test_set = dataset[int(len(dataset) * 0.75):]

    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]
    test_X = encoder.transform(test_X)

    classifier = CategoricalNB()
    classifier.fit(train_X, train_Y)

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_X[i]])[0]
        true_class = test_Y[i]

        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)

    print(accuracy)

    entry = [e for e in input().split(" ")]


    encoded_entry = encoder.transform([entry])

    predicted_class = classifier.predict(encoded_entry)

    print(predicted_class[0])

    print(classifier.predict_proba(encoded_entry))

# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

# submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_X)

# submit na klasifikatorot
    submit_classifier(classifier)

# submit na encoderot
    submit_encoder(encoder)
