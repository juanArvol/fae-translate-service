from pathlib import Path

import argostranslate.package


MODEL_PACKAGES_DIR = Path("/app/models")


def install_models():

    model_files = list(
        MODEL_PACKAGES_DIR.glob("*.argosmodel")
    )

    if not model_files:
        raise RuntimeError(
            "No se encontraron archivos .argosmodel"
        )

    for model_path in model_files:

        print(
            f"Instalando modelo: {model_path.name}"
        )

        argostranslate.package.install_from_path(
            model_path
        )

        print(
            f"Modelo instalado: {model_path.name}"
        )


if __name__ == "__main__":
    install_models()