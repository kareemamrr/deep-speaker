import numpy as np
import random

from numpy.core.numeric import identity
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
        self.database = {}
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
        self.database[name] = audio

    def verify(self, audio, name):
        identity_embed = self.database[name]
        audio1, audio2 = audio
        mfcc = self.gen_mfcc(audio)
        test_embed = self.gen_embedding(mfcc)
        score = self.get_score([identity_embed, test_embed])
        if score > self.threshold:
            return 1
        else:
            return 0