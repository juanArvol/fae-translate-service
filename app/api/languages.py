from fastapi import APIRouter

import argostranslate.translate


router = APIRouter()


@router.get("/languages")
def get_languages():

    languages = argostranslate.translate.get_installed_languages()

    return {
        "languages": [
            {
                "code": language.code,
                "name": language.name
            }
            for language in languages
        ]
    }