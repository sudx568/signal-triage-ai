class DecisionEngine:


    def decide(self, prediction):

        confidence = prediction.confidence


        if confidence >= 0.75:

            return "AUTO_PROCESS"


        elif confidence >= 0.45:

            return "HUMAN_REVIEW"


        else:

            return "NEEDS_MORE_INFO"