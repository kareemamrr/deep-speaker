from backend import Model
import io
import soundfile as sf
from fastapi import FastAPI, File, Form, UploadFile, Request
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


@app.post("/save")
def save(username: str = Form(...), file: UploadFile = File(...)):
    audio_bytes = file.file.read()
    signal, sr = sf.read(io.BytesIO(audio_bytes))
    return f'{sr}'
    # with open(f'uploads/{username}.wav', "bx") as buffer:
    #     buffer.write(audio_bytes)


@app.get("/")
def read_root(request: Request):
    return 'Head to /docs endpoint'


@app.post("/enroll")
def enroll_user(uploadedfile: UploadFile = File(...), username: str = Form(...)):
    model.enroll(uploadedfile.file, username)
    return "user profile added"


@app.delete("/delete")
def remove_user(username: str = Form(...)):
    model.remove_embedding(username)
    return "user profile removed"


@app.put("/update")
def update_user_voiceprint(
    uploadedfile: UploadFile = File(...), username: str = Form(...)
):
    model.enroll(uploadedfile.file, username)
    return "user profile updated"


@app.post("/verify")
def verify_user_identity(
    uploadedfile: UploadFile = File(...),
    username: str = Form(...),
    label: int = Form(...),
):
    return model.verify(uploadedfile.file, username, label)


@app.get("/db")
def view_enrolled_users():
    return model.users
