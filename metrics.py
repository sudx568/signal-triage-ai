from sklearn.metrics import (
    accuracy_score,
    classification_report
)



def evaluate(actual, predicted, method_name="Model"):


    accuracy = accuracy_score(
        actual,
        predicted
    )


    print("=" * 50)

    print(method_name)

    print(
        "Accuracy:",
        round(accuracy * 100, 2),
        "%"
    )


    print()

    print(
        classification_report(
            actual,
            predicted,
            zero_division=0
        )
    )


    return accuracy