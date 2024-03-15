from pydantic import BaseModel

class ParaphraseRequest(BaseModel):
    texts: list[str]
    num_return_sequences: int = 3

class ParaphraseResponse(BaseModel):
    paraphrases: list[list[str]]