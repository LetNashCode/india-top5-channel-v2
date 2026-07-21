import whisper

_model = None


def _get_model():
    global _model

    if _model is None:
        _model = whisper.load_model("base")

    return _model


def transcribe(audio_path):
    model = _get_model()

    result = model.transcribe(
        audio_path,
        word_timestamps=True,
        fp16=False,
    )

    words = []

    for segment in result["segments"]:
        for word in segment.get("words", []):
            words.append(
                {
                    "word": word["word"].strip(),
                    "start": word["start"],
                    "end": word["end"],
                }
            )

    return words
