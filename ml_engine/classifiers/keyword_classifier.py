"""
Keyword-based classifier.

This classifier predicts the category of a signal using
predefined keyword matching.
"""

import re
from typing import Dict

from ml_engine.classifiers.base import BaseClassifier, Prediction


class KeywordClassifier(BaseClassifier):

    KEYWORDS: Dict[str, list] = {
        "billing": [
            "payment",
            "refund",
            "invoice",
            "charged",
            "billing",
            "subscription",
            "renewal",
            "fee",
            "gst",
            "tax",
        ],
        "bug": [
            "bug",
            "error",
            "crash",
            "issue",
            "freeze",
            "broken",
            "loading",
            "failed",
            "exception",
            "problem",
        ],
        "feature_request": [
            "feature",
            "add",
            "support",
            "would like",
            "please add",
            "can you",
            "enhancement",
            "improve",
            "option",
            "allow",
        ],
        "spam": [
            "winner",
            "free",
            "click",
            "offer",
            "money",
            "crypto",
            "casino",
            "loan",
            "gift",
            "reward",
        ],
        "urgent_complaint": [
            "urgent",
            "critical",
            "immediately",
            "blocked",
            "down",
            "asap",
            "angry",
            "complaint",
            "security",
            "breach",
        ],
    }

    def preprocess(self, text: str) -> str:
        """
        Basic preprocessing.
        """
        text = text.lower().strip()
        text = re.sub(r"[^\w\s]", " ", text)
        return text

    def predict(self, text: str) -> Prediction:

        text = self.preprocess(text)

        if not text:
            return Prediction(
                label="unknown",
                confidence=0.0,
                classifier_name="KeywordClassifier",
                metadata={"reason": "Empty input"},
            )

        scores = {}
        matched_keywords = {}

        for label, keywords in self.KEYWORDS.items():

            matches = [kw for kw in keywords if kw in text]

            scores[label] = len(matches)
            matched_keywords[label] = matches

        best_label = max(scores, key=scores.get)
        best_score = scores[best_label]

        if best_score == 0:
            return Prediction(
                label="unknown",
                confidence=0.0,
                classifier_name="KeywordClassifier",
                metadata={
                    "scores": scores,
                    "matched_keywords": matched_keywords,
                },
            )

        confidence = round(
            best_score / len(self.KEYWORDS[best_label]),
            2,
        )

        return Prediction(
            label=best_label,
            confidence=confidence,
            classifier_name="KeywordClassifier",
            metadata={
                "scores": scores,
                "matched_keywords": matched_keywords,
            },
        )