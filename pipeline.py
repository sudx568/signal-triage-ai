"""
Main pipeline entry point.
"""

from config import DATASET_PATH, CONFIDENCE_THRESHOLD

from data.loader import DataLoader

from ml_engine.classifiers.keyword_classifier import KeywordClassifier
from ml_engine.classifiers.embedding_classifier import EmbeddingClassifier

from decision_engine import DecisionEngine

from metrics import evaluate

from utils.logger import get_logger


logger = get_logger()


# Load dataset

loader = DataLoader(DATASET_PATH)

df = loader.load()


# Initialize classifiers

keyword_classifier = KeywordClassifier()

embedding_classifier = EmbeddingClassifier()


# Initialize decision engine

decision_engine = DecisionEngine()


# Metrics storage

actual_labels = []

predicted_labels = []


print("=" * 60)
print("SIGNAL TRIAGE PIPELINE STARTED")
print("=" * 60)



for _, row in df.iterrows():

    text = row["text"]


    # Actual label from dataset

    actual_labels.append(
        row["ground_truth"]
    )


    # Step 1:
    # Try keyword classifier first

    prediction = keyword_classifier.predict(text)



    # Step 2:
    # If confidence is low,
    # use embedding classifier

    if (
        prediction.label == "unknown"
        or prediction.confidence < CONFIDENCE_THRESHOLD
    ):

        prediction = embedding_classifier.predict(text)



    # Save prediction

    predicted_labels.append(
        prediction.label
    )



    # Step 3:
    # Decision layer

    action = decision_engine.decide(
        prediction
    )



    # Logging

    logger.info(
        f"ID={row['id']} | "
        f"Prediction={prediction.label} | "
        f"Confidence={prediction.confidence} | "
        f"Classifier={prediction.classifier_name} | "
        f"Action={action}"
    )



    # Console output

    print(f"Message      : {text}")
    print(f"Actual       : {row['ground_truth']}")
    print(f"Predicted    : {prediction.label}")
    print(f"Confidence   : {prediction.confidence}")
    print(f"Classifier   : {prediction.classifier_name}")
    print(f"Action       : {action}")
    print("-" * 60)



print("=" * 60)

print("Evaluation Results")

evaluate(
    actual_labels,
    predicted_labels
)


print("=" * 60)

print("Pipeline completed successfully.")