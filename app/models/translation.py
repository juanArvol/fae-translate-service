from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    text: str = Field(min_length=1)
    source: str
    target: str


class BatchTranslationRequest(BaseModel):
    texts: list[str] = Field(min_length=1)
    source: str
    target: str