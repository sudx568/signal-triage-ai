# Signal Triage AI - Evaluation Report

## 1. Introduction

Signal Triage AI is an intelligent text classification system designed to automatically categorize and prioritize incoming customer messages. The objective of this project is to reduce manual support effort by using multiple classification approaches and automatically escalating uncertain cases for human review.

The system uses a hybrid approach combining a keyword-based classifier and an embedding similarity classifier. Predictions from both methods are evaluated, compared, and passed through a decision engine that determines whether a message can be automatically processed or requires human intervention.

---

## 2. Dataset Description

The system uses a dataset containing short customer messages across multiple categories such as billing issues, technical problems, feature requests, spam, and urgent complaints.

Each message contains:
- Text input
- Ground truth category label

The dataset is used for evaluating classifier performance and measuring escalation behavior.

---

## 3. Classification Methods

### Keyword Classifier

The keyword classifier uses predefined domain-specific terms to identify categories. It is fast, interpretable, and suitable for clear messages containing important keywords.

However, it has limitations when users describe the same issue using different words.

Example:
"Money deducted but transaction failed"

may not always contain exact billing keywords.

### Embedding Similarity Classifier

The embedding classifier converts text into numerical representations and compares semantic similarity between messages and known examples.

This approach understands different wording patterns and improves classification for more natural user messages.

### Hybrid Approach

The final system compares both classifier outputs and selects the prediction with stronger confidence. This improves reliability compared to using a single method.

---

## 4. Escalation Logic

The system uses two conditions for human review:

1. Low confidence prediction

If the confidence score is below the defined threshold of 0.75, the message is escalated.

2. Classifier disagreement

If keyword and embedding classifiers produce different categories, the system routes the message to human review.

This prevents incorrect automatic decisions.

---

## 5. Threshold Reasoning

A confidence threshold of 0.75 was selected to balance automation and reliability.

A lower threshold could increase automatic processing but may allow incorrect classifications. A higher threshold would improve reliability but create unnecessary human workload.

The selected threshold allows high-confidence cases to be processed automatically while uncertain cases receive human validation.

---

## 6. Method Comparison

The evaluation compares:

- Keyword classifier accuracy
- Embedding classifier accuracy
- Hybrid system accuracy

The comparison helps identify the strengths and weaknesses of each approach.

Keyword methods provide speed and interpretability, while embedding methods provide better semantic understanding.

---

## 7. Future Improvements

With additional time, the system could be improved by:

- Training domain-specific machine learning models
- Adding real customer support datasets
- Storing predictions in a database
- Creating analytics dashboards
- Using human feedback to continuously improve classification

---

## Conclusion

Signal Triage AI demonstrates how multiple AI approaches can work together to create a reliable classification system. By combining different methods with confidence-based escalation, the system improves automation while maintaining human oversight for uncertain cases.