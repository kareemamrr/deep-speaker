from backend import Model
import shutil
from fastapi import FastAPI, File, Form, UploadFile, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

model = Model()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

origins = ["http://127.0.0.1:5500", "http://127.0.0.1:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/save")
async def save(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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
