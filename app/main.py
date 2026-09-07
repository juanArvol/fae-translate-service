from fastapi import FastAPI

from app.api.translation import router as translation_router
from app.api.languages import router as languages_router


app = FastAPI(
    title="FAE Translation Service",
    version="1.0.0"
)


app.include_router(translation_router)
app.include_router(languages_router)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }