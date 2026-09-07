from fastapi import APIRouter, HTTPException

from app.models.translation import (
    TranslationRequest,
    BatchTranslationRequest
)

from app.services.translation_service import TranslationService


router = APIRouter()

translation_service = TranslationService()


@router.post("/translate")
def translate(request: TranslationRequest):

    try:

        translated_text = translation_service.translate(
            request.text,
            request.source,
            request.target
        )

        return {
            "translatedText": translated_text
        }

    except ValueError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )

    except RuntimeError as exc:

        raise HTTPException(
            status_code=422,
            detail=str(exc)
        )


@router.post("/translate/batch")
def translate_batch(request: BatchTranslationRequest):

    try:

        translations = [
            translation_service.translate(
                text,
                request.source,
                request.target
            )
            for text in request.texts
        ]

        return {
            "translations": translations
        }

    except ValueError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )

    except RuntimeError as exc:

        raise HTTPException(
            status_code=422,
            detail=str(exc)
        )