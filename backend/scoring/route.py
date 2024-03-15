from fastapi import APIRouter, HTTPException
from .dependencies import get_scores
from .schemas import ScoringRequest, ScoringResponse

router = APIRouter()

@router.post("/scores/")

async def scoring(request: ScoringRequest):
    try:
        scores = get_scores(request.answers, request.references, request.max_score)
        return ScoringResponse(scores=scores)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))