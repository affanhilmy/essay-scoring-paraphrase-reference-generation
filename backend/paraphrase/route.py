from dotenv import load_dotenv
from pathlib import Path
import os
from fastapi import APIRouter, HTTPException
from .dependencies import generate_paraphrase
from .schemas import ParaphraseRequest, ParaphraseResponse

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

router = APIRouter()

@router.post("/paraphrase/")
async def paraphrase_text(request: ParaphraseRequest):
    try:
        model_directory = os.getenv("PARAPHRASE_MODEL")
        generated_paraphrases = generate_paraphrase(model_directory, request.texts, request.num_return_sequences)
        return ParaphraseResponse(paraphrases=generated_paraphrases)
    except Exception as r:
        raise HTTPException(status_code=500, detail=str(r))