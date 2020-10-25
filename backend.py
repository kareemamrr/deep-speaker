import numpy as np
import random

from audio import read_mfcc
from batcher import sample_from_mfcc
from constants import SAMPLE_RATE, NUM_FRAMES
from conv_models import DeepSpeakerModel
from test import batch_cosine_similarity
import logging

np.random.seed(123)
random.seed(123)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs.log")
formatter = logging.Formatter("%(asctime)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Model:
    def __init__(self):
        self.threshold = 0.7
        self._database = {}
        self.users = []
        self.model = DeepSpeakerModel()
        self.model.m.load_weights("ResCNN_checkpoint_850.h5", by_name=True)

    def gen_mfcc(self, audio):
        return sample_from_mfcc(read_mfcc(audio, SAMPLE_RATE), NUM_FRAMES)

    def gen_embedding(self, mfcc):
        return self.model.m.predict(np.expand_dims(mfcc, axis=0))

    def get_score(self, embeds):
        return batch_cosine_similarity(embeds[0], embeds[1])

    def enroll(self, audio, name):
        mfcc = self.gen_mfcc(audio)
        embed = self.gen_embedding(mfcc)
        self._database[name] = embed
        if name not in self.users:
            self.users.append(name)

    def verify(self, audio, name, label):
        identity_embed = self._database[name]
        mfcc = self.gen_mfcc(audio)
        test_embed = self.gen_embedding(mfcc)
        score = self.get_score([identity_embed, test_embed])
        if score > self.threshold:
            prediction = 1
        else:
            prediction = 0
        self.log_info(label, prediction, score)
        return prediction

    def remove_embedding(self, name):
        self._database.pop(name)
        self.users.remove(name)

    def log_info(self, label, prediction, score):
        logger.info(f"Label -> {label}")
        logger.info(f"Prediction -> {prediction}")
        logger.info(f"Result -> {label == prediction}")
        logger.info(f"Similarity score -> {score}")
        logger.info(f"Threshold -> {self.threshold}")
        logger.info("**************************************")