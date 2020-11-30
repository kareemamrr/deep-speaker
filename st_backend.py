import numpy as np
import random
from audio import read_mfcc
from batcher import sample_from_mfcc
from constants import SAMPLE_RATE, NUM_FRAMES
from conv_models import DeepSpeakerModel
from test import batch_cosine_similarity

np.random.seed(123)
random.seed(123)

model = DeepSpeakerModel()
model.m.load_weights("ResCNN_checkpoint_850.h5", by_name=True)


class Model():
    @staticmethod
    def gen_mfcc(audio):
        return sample_from_mfcc(read_mfcc(audio, SAMPLE_RATE), NUM_FRAMES)

    @staticmethod
    def gen_embedding(mfcc):
        return model.m.predict(np.expand_dims(mfcc, axis=0))

    @staticmethod
    def get_score(embeds):
        return batch_cosine_similarity(embeds[0], embeds[1])

    @staticmethod
    def enroll(audio, name):
        mfcc = Model.gen_mfcc(audio)
        embed = Model.gen_embedding(mfcc)
        Model.store_embedding(name, embed)

    @staticmethod
    def verify(audio, name):
        identity_embed = Model.load_embedding(name)
        mfcc = Model.gen_mfcc(audio)
        test_embed = Model.gen_embedding(mfcc)
        score = Model.get_score([identity_embed, test_embed])
        if score > 0.7:
            return 1
        else:
            return 0

    @staticmethod
    def store_embedding(name, embedding):
        np.save(f'embeddings/{name}.npy', embedding)

    @staticmethod
    def load_embedding(name):
        return np.load(f'embeddings/{name}.npy')
