import random
import numpy as np
from audio import read_mfcc
from batcher import sample_from_mfcc
from constants import SAMPLE_RATE, NUM_FRAMES
from conv_models import DeepSpeakerModel
from test import batch_cosine_similarity

np.random.seed(123)
random.seed(123)


def get_embedding(audio_file):
    model = DeepSpeakerModel()
    path = "ResCNN_checkpoint_850.h5"

    model.m.load_weights(path, by_name=True)

    mfcc = sample_from_mfcc(read_mfcc(audio_file, SAMPLE_RATE), NUM_FRAMES)

    embedding = model.m.predict(np.expand_dims(mfcc, axis=0))
    return embedding


def verify_identity(database, audio_file, username, threshold):
    identity_embedding = database[username]
    test_embedding = get_embedding(audio_file)
    similarity = batch_cosine_similarity(identity_embedding, test_embedding)
    if similarity > threshold:
        return 1
    else:
        return 0
