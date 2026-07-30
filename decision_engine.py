class DecisionEngine:

    CONFIDENCE_THRESHOLD = 0.75


    def decide(
        self,
        prediction,
        keyword_prediction=None,
        embedding_prediction=None
    ):

        confidence = prediction.confidence


        # Check classifier disagreement
        if (
            keyword_prediction
            and embedding_prediction
            and keyword_prediction != embedding_prediction
        ):

            return {
                "action": "HUMAN_REVIEW",
                "reason": "Classifier disagreement",
                "confidence": confidence
            }


        # Check confidence threshold
        if confidence >= self.CONFIDENCE_THRESHOLD:

            return {
                "action": "AUTO_PROCESS",
                "reason": "High confidence prediction",
                "confidence": confidence
            }


        elif confidence >= 0.45:

            return {
                "action": "HUMAN_REVIEW",
                "reason": "Low confidence prediction",
                "confidence": confidence
            }


        else:

            return {
                "action": "NEEDS_MORE_INFO",
                "reason": "Very low confidence",
                "confidence": confidence
            }