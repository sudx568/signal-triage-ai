from config import CONFIDENCE_THRESHOLD

from ml_engine.classifiers.keyword_classifier import KeywordClassifier
from ml_engine.classifiers.embedding_classifier import EmbeddingClassifier

from decision_engine import DecisionEngine


keyword_classifier = KeywordClassifier()
embedding_classifier = EmbeddingClassifier()
decision_engine = DecisionEngine()


def predict_signal(text: str):

    # Run keyword classifier first
    keyword_prediction = keyword_classifier.predict(text)

    # Default embedding prediction
    embedding_prediction = keyword_prediction

    # Run embedding classifier if needed
    if (
        keyword_prediction.label == "unknown"
        or keyword_prediction.confidence < CONFIDENCE_THRESHOLD
    ):
        embedding_prediction = embedding_classifier.predict(text)

    # Select final prediction
    if embedding_prediction.confidence > keyword_prediction.confidence:
        prediction = embedding_prediction
    else:
        prediction = keyword_prediction

    # Decision Engine
    decision = decision_engine.decide(
        prediction,
        keyword_prediction.label,
        embedding_prediction.label
    )

    # Priority Logic
    if prediction.confidence < 0.50:
        priority = "high"
    elif prediction.confidence < 0.75:
        priority = "normal"
    else:
        priority = "low"

    # IMPORTANT:
    # FastAPI expects action as STRING
    action = decision["action"]

    return {
        "text": text,
        "category": prediction.label,
        "confidence": prediction.confidence,
        "classifier": prediction.classifier_name,
        "action": action,
        "priority": priority
    }
