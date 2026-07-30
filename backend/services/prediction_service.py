from config import CONFIDENCE_THRESHOLD

from ml_engine.classifiers.keyword_classifier import KeywordClassifier
from ml_engine.classifiers.embedding_classifier import EmbeddingClassifier

from decision_engine import DecisionEngine



keyword_classifier = KeywordClassifier()

embedding_classifier = EmbeddingClassifier()

decision_engine = DecisionEngine()



def predict_signal(text: str):


    prediction = keyword_classifier.predict(text)



    if (
        prediction.label == "unknown"
        or prediction.confidence < CONFIDENCE_THRESHOLD
    ):

        prediction = embedding_classifier.predict(text)



    action = decision_engine.decide(
        prediction
    )


    priority = "normal"


    if prediction.confidence < 0.5:
        priority = "high"


    elif prediction.confidence > 0.8:
        priority = "low"



    return {

        "text": text,

        "category": prediction.label,

        "confidence": prediction.confidence,

        "classifier": prediction.classifier_name,

        "action": action,

        "priority": priority

    }