import argostranslate.translate


class TranslationService:

    def translate(
        self,
        text: str,
        source: str,
        target: str
    ) -> str:

        text = text.strip()

        if not text:
            raise ValueError("Translation text cannot be empty")

        if source == target:
            return text

        try:
            return argostranslate.translate.translate(
                text,
                source,
                target
            )

        except Exception as exc:
            raise RuntimeError(
                f"Translation failed: {source} -> {target}"
            ) from exc