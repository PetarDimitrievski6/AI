import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.ensemble import RandomForestClassifier

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    # Vashiot kod tuka

    col_index = int(input())

    dataset = [[t[i] for i in range(len(t)) if i != col_index] for t in dataset]

    train_set = dataset[:int(len(dataset) * 0.85)]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_set = dataset[int(len(dataset) * 0.85):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    num_trees = int(input())
    criterion = input()
    classifier = RandomForestClassifier(n_estimators=num_trees, criterion=criterion, random_state=0)
    classifier.fit(train_X, train_Y)

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_X[i]])[0]
        true_class = test_Y[i]

        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)

    print(f"Accuracy: {accuracy}")

    entry = [float(n) for n in input().split(' ')]
    entry = [entry[i] for i in range(len(entry)) if i != col_index]

    print(classifier.predict([entry])[0])
    print(classifier.predict_proba([entry])[0])

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)
