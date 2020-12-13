from backend import Model
from backend import Model
import os
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware

model = Model()

app = FastAPI()

origins = ["http://127.0.0.1:5500", "http://127.0.0.1:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def store_audio(audio, username):
    audio_bytes = audio.file.read()
    path = f"uploads/{username}.wav"
    with open(path, mode="bx") as f:
        f.write(audio_bytes)
    return path


def clear_audio_embeddings():
    [os.remove(f"uploads/{file}") for file in os.listdir("uploads")]


@app.get("/")
def read_root():
    return "Head to /docs endpoint"


@app.get("/clear")
def clear_embeddings_cache():
    [os.remove(f"embeddings/{file}") for file in os.listdir("embeddings")]
    return "Cache cleared"


@app.post("/enroll")
def enroll_user(audio: UploadFile = File(...), username: str = Form(...)):
    path = store_audio(audio, username)
    Model.enroll(path, username)
    clear_audio_embeddings()
    return "user profile added"


@app.post("/verify")
def verify_user_identity(audio: UploadFile = File(...), username: str = Form(...)):
    path = store_audio(audio, username)
    pred = Model.verify(path, username)
    clear_audio_embeddings()
    return pred


@app.get("/db")
def view_enrolled_users():
    return model.users
