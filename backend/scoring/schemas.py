from pydantic import BaseModel

class ScoringRequest(BaseModel):
    answers: list[str]
    references: list[str]
    max_score: int = 10

class ScoringResponse(BaseModel):
    scores: list[float]