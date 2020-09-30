import numpy as np
import random
from audio import read_mfcc
from batcher import sample_from_mfcc
from constants import SAMPLE_RATE, NUM_FRAMES
from conv_models import DeepSpeakerModel
from test import batch_cosine_similarity

np.random.seed(123)
random.seed(123)


class Model:
    def __init__(self):
        self.threshold = 0.7
        self.model = DeepSpeakerModel()
        self.model.m.load_weights("ResCNN_checkpoint_850.h5", by_name=True)

    def gen_mfcc(self, path):
        return sample_from_mfcc(read_mfcc(path, SAMPLE_RATE), NUM_FRAMES)

    def gen_embedding(self, mfcc):
        return self.model.m.predict(np.expand_dims(mfcc, axis=0))

    def get_score(self, embeds):
        return batch_cosine_similarity(embeds[0], embeds[1])

    def predict(self, paths):
        path1, path2 = paths
        mfcc1, mfcc2 = self.gen_mfcc(path1), self.gen_mfcc(path2)
        embed1, embed2 = self.gen_embedding(mfcc1), self.gen_embedding(mfcc2)
        score = self.get_score([embed1, embed2])
        if score > self.threshold:
            return [score, 1]
        else:
            return [score, 0]