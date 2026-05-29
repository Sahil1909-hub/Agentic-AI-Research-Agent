from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import shutil
import os
from app.workflow.graph import app_graph

router = APIRouter()

UPLOAD_DIR = "data/uploaded_pdfs"

os.makedirs(UPLOAD_DIR, exist_ok=True)


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    try:

        result = app_graph.invoke({
            "question": request.question
        })

        print("GRAPH RESULT:", result)

        return {
            "response": result.get("answer", "No answer generated")
        }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            "error": str(e)
        }

@router.post("/upload-pdf")
def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "PDF Uploaded Successfully",
        "file_path": file_path
    }