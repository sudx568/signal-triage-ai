from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from ml_engine.classifiers.base import BaseClassifier, Prediction


class EmbeddingClassifier(BaseClassifier):

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )


        self.examples = {

            "billing": [
                "payment issue",
                "refund problem",
                "wrong invoice",
                "charged incorrectly",
                "subscription payment",
                "duplicate transaction",
                "billing problem",
                "payment failed",
                "charged twice",
                "card payment issue"
            ],


            "bug": [
                "application crash",
                "feature not working",
                "software error",
                "app problem",
                "system failure",
                "login not working",
                "screen frozen",
                "upload failed",
                "button does not work",
                "application error"
            ],


            "feature_request": [
                "add new feature",
                "request improvement",
                "please add option",
                "support new functionality",
                "add dark mode",
                "need new settings",
                "add export option",
                "support more features"
            ],


            "spam": [
                "free prize",
                "win money",
                "click this link",
                "limited offer",
                "earn money fast",
                "claim reward",
                "free gift",
                "special deal"
            ],


            "urgent_complaint": [
                "critical issue",
                "service down",
                "business blocked",
                "urgent support",
                "production outage",
                "security issue",
                "account locked",
                "immediate resolution"
            ]

        }


        self.labels = []

        self.embeddings = []


        for label, texts in self.examples.items():

            for text in texts:

                self.labels.append(label)

                self.embeddings.append(
                    self.model.encode(text)
                )



    def predict(self, text):

        query_embedding = self.model.encode(text)


        scores = cosine_similarity(
            [query_embedding],
            self.embeddings
        )[0]


        best_index = scores.argmax()


        confidence = float(
            scores[best_index]
        )


        if confidence < 0.35:

            return Prediction(
                label="unknown",
                confidence=confidence,
                classifier_name="embedding"
            )


        return Prediction(
            label=self.labels[best_index],
            confidence=confidence,
            classifier_name="embedding"
        )