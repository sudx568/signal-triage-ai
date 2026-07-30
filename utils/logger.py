import logging


def get_logger():

    logger = logging.getLogger("SignalPipeline")

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(message)s"

    )

    file_handler = logging.FileHandler(

        "logs/pipeline.log"

    )

    file_handler.setFormatter(formatter)

    if not logger.handlers:

        logger.addHandler(file_handler)

    return logger