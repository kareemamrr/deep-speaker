import random
import logging
import glob
from example import Model

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs.log")
formatter = logging.Formatter("%(asctime)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def log_info(label, prediction, score, threshold):
    logger.info(f"Label -> {label}")
    logger.info(f"Prediction -> {prediction}")
    logger.info(f"Result -> {label == prediction}")
    logger.info(f"Similarity score -> {score}")
    logger.info(f"Threshold -> {threshold}")
    logger.info("**************************************")


def get_file_paths(dir):
    return glob.glob(f"{dir}/**/*.wav")


if __name__ == "__main__":
    model = Model()
    for i in range(20):
        files = get_file_paths("samples")
        audio_pair = random.sample(files, k=2)
        ids = [audio.split("/")[1] for audio in audio_pair]
        if ids[0] == ids[1]:
            label = 1
        else:
            label = 0
        score, prediction = model.predict(audio_pair)
        log_info(label, prediction, score, 0.7)