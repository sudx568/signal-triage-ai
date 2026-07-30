from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


def evaluate(actual, predicted):

    print(
        "Accuracy:",
        accuracy_score(
            actual,
            predicted
        )
    )


    print(
        classification_report(
            actual,
            predicted,
            zero_division=0
        )
    )