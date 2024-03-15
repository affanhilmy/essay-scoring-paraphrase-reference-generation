from fastapi import FastAPI
from backend.paraphrase.route import router as ParaphraseRouter
from backend.scoring.route import router as ScoringRouter

app = FastAPI()

version = "/api/v1"
app.include_router(ParaphraseRouter, prefix=version)
app.include_router(ScoringRouter, prefix=version)