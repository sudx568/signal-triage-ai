import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

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

CONFIDENCE_THRESHOLD = 0.70

OLLAMA_MODEL = "llama3"