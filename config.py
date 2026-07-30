import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


DATASET_PATH = os.path.join(
    BASE_DIR,
    "data",
    "signals.csv"
)


LOG_FILE = os.path.join(
    BASE_DIR,
    "logs",
    "pipeline.log"
)


# Confidence below this value goes for human review
# Chosen to balance automation and accuracy
CONFIDENCE_THRESHOLD = 0.75


OLLAMA_MODEL = "llama3"