
from deep_translator import GoogleTranslator

def translate(text: str, direction="en-ne") -> str:
    if not text.strip():
        return ""
    try:
        if direction == "en-ne":
            return GoogleTranslator(source='en', target='ne').translate(text)
        else:
            return GoogleTranslator(source='ne', target='en').translate(text)
    except Exception:
        return f"[error] translation failed"
