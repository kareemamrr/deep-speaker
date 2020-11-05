from backend import Model
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()
model = Model()


@app.get("/")
def read_root():
    return {"Please redirect to /docs endpoint testing"}


@app.post("/enroll")
def enroll_user(uploadedfile: UploadFile = File(...), username: str = Form(...)):
    model.enroll(uploadedfile.file, username)
    return "user profile added"


@app.delete("/delete")
def remove_user(username: str = Form(...)):
    model.remove_embedding(username)
    return "user profile removed"


@app.put("/update")
def update_user_voiceprint(uploadedfile: UploadFile = File(...), username: str = Form(...)):
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
