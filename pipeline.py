"""
Main Signal Triage Evaluation Pipeline
"""

from config import DATASET_PATH

from data.loader import DataLoader

from ml_engine.classifiers.keyword_classifier import KeywordClassifier
from ml_engine.classifiers.embedding_classifier import EmbeddingClassifier

from decision_engine import DecisionEngine

from metrics import evaluate

from utils.logger import get_logger

import csv
import os


logger = get_logger()


# Load dataset

loader = DataLoader(DATASET_PATH)

df = loader.load()



# Initialize classifiers

keyword_classifier = KeywordClassifier()

embedding_classifier = EmbeddingClassifier()



# Decision engine

decision_engine = DecisionEngine()



actual_labels = []

keyword_predictions = []

embedding_predictions = []

hybrid_predictions = []


human_review_queue = []



print("=" * 60)
print("SIGNAL TRIAGE PIPELINE STARTED")
print("=" * 60)



for _, row in df.iterrows():


    text = row["text"]

    actual = row["ground_truth"]


    actual_labels.append(actual)



    # Run BOTH classifiers

    keyword_result = keyword_classifier.predict(text)

    embedding_result = embedding_classifier.predict(text)



    keyword_predictions.append(
        keyword_result.label
    )


    embedding_predictions.append(
        embedding_result.label
    )



    # Choose final prediction

    if keyword_result.confidence >= embedding_result.confidence:

        final_prediction = keyword_result

    else:

        final_prediction = embedding_result



    hybrid_predictions.append(
        final_prediction.label
    )



    # Decision with disagreement check

    decision = decision_engine.decide(

        final_prediction,

        keyword_result.label,

        embedding_result.label

    )



    print("="*60)

    print("Message:", text)

    print("Actual:", actual)

    print(
        "Keyword:",
        keyword_result.label,
        keyword_result.confidence
    )

    print(
        "Embedding:",
        embedding_result.label,
        embedding_result.confidence
    )


    print(
        "Final:",
        final_prediction.label
    )


    print(
        "Action:",
        decision["action"]
    )


    print(
        "Reason:",
        decision["reason"]
    )



    # Store human review cases

    if decision["action"] == "HUMAN_REVIEW":


        human_review_queue.append({

            "text": text,

            "reason": decision["reason"],

            "confidence": decision["confidence"]

        })




# Save human review queue


os.makedirs(
    "data",
    exist_ok=True
)


with open(
    "data/human_review_queue.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:


    writer = csv.DictWriter(

        file,

        fieldnames=[
            "text",
            "reason",
            "confidence"
        ]

    )


    writer.writeheader()

    writer.writerows(
        human_review_queue
    )




print("\nEvaluation Results")



print("\nKeyword Classifier")

evaluate(
    actual_labels,
    keyword_predictions,
    "Keyword Classifier"
)



print("\nEmbedding Classifier")

evaluate(
    actual_labels,
    embedding_predictions,
    "Embedding Classifier"
)


print("\nHybrid System")

evaluate(
    actual_labels,
    hybrid_predictions,
    "Hybrid System"
)


print(
    "\nEscalated Cases:",
    len(human_review_queue)
)


print(
    "Escalation Rate:",
    round(
        len(human_review_queue)/len(df)*100,
        2
    ),
    "%"
)



print("=" * 60)

print("Pipeline completed successfully.")