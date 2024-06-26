import csv
from sklearn.naive_bayes import GaussianNB

def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]

    dataset = [[float(element) for element in row] for row in dataset]

    return dataset


if __name__ == '__main__':
    dataset = read_file("medical_data.csv")

    train_set = dataset[:int(len(dataset) * 0.7)]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(len(dataset) * 0.7):]
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

    accuracy = accuracy / len(test_set)

    print(f"Accuracy: {accuracy}")

    entry = [float(e) for e in input().split(" ")]

    predicted_class = classifier.predict([entry])[0]

    print(predicted_class)
