import whisper
import os

WHISPER_MODEL = os.getenv("WHISPER_MODEL", "small")

_model = None


def load_model():
    global _model

    if _model is None:
        print("Loading Whisper model...")
        _model = whisper.load_model(WHISPER_MODEL)
        print("Whisper model loaded successfully")

    return _model


def transcribe_chunk(
    chunk_path: str,
    language: str = "auto",
    translate: bool = False
) -> str:

    model = load_model()

    # Whisper language codes
    language_codes = {
        "english": "en",
        "urdu": "ur"
    }

    selected_language = language_codes.get(language.lower())

    options = {
        "task": "translate" if translate else "transcribe"
    }

    # Auto-detect when language is "auto"
    if selected_language:
        options["language"] = selected_language

    result = model.transcribe(chunk_path, **options)

    return result["text"].strip()


def transcribe_all(
    chunks: list,
    language: str = "auto",
    translate: bool = False
) -> str:

    full_transcript = ""

    for i, chunk in enumerate(chunks):
        print(f"Transcribing chunk {i + 1}/{len(chunks)}...")

        text = transcribe_chunk(
            chunk,
            language=language,
            translate=translate
        )

        full_transcript += text + " "

    print("Transcription completed")

    return full_transcript.strip()