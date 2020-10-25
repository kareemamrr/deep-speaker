from backend import Model
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()
model = Model()


@app.get("/")
def read_root():
    return {"Hello World"}


@app.post("/enroll")
def enroll_user(uploadedfile: UploadFile = File(...), username: str = Form(...)):
    model.enroll(uploadedfile.file, username)
    return "user profile added"


@app.put("/delete")
def remove_user(username: str = Form(...)):
    model.remove_embedding(username)
    return "user profile removed"


@app.put("/update")
def update_user(uploadedfile: UploadFile = File(...), username: str = Form(...)):
    model.enroll(uploadedfile.file, username)
    return "user profile updated"


@app.post("/verify")
def verify_user(
    uploadedfile: UploadFile = File(...),
    username: str = Form(...),
    label: int = Form(...),
):
    return model.verify(uploadedfile.file, username, label)


@app.get("/db")
def view_db():
    return model.users
