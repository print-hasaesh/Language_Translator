"""
translator_engine.py

Provides a simple `translate(text, direction)` function.
It tries to use `googletrans` and falls back to a tiny dictionary when unavailable.
"""

from typing import Optional

try:
    from googletrans import Translator as _GoogleTranslator
except Exception:
    _GoogleTranslator = None


# small fallback dictionary for common words/phrases
_EN_TO_NE = {
    "hello": "नमस्कार",
    "hi": "नमस्ते",
    "how are you": "तिमीलाई कस्तो छ",
    "thank you": "धन्यवाद",
    "yes": "हो",
    "no": "होइन",
    "good morning": "शुभप्रभात",
}

_NE_TO_EN = {v: k for k, v in _EN_TO_NE.items()}


def _fallback_translate(text: str, direction: str) -> str:
    t = text.strip().lower()
    if direction == "en-ne":
        return _EN_TO_NE.get(t, f"[no-fallback] {text}")
    else:
        return _NE_TO_EN.get(t, f"[no-fallback] {text}")


def translate(text: str, direction: str = "en-ne") -> str:
    """
    Translate `text`.

    direction: 'en-ne' or 'ne-en'
    Returns translated string.
    Uses googletrans if available, otherwise fallback dictionary.
    """
    if not text:
        return ""

    if _GoogleTranslator is None:
        return _fallback_translate(text, direction)

    src = "en" if direction == "en-ne" else "ne"
    dest = "ne" if direction == "en-ne" else "en"

    try:
        g = _GoogleTranslator()
        res = g.translate(text, src=src, dest=dest)
        return res.text
    except Exception:
        return _fallback_translate(text, direction)


if __name__ == "__main__":
    # quick smoke test
    print(translate("hello", "en-ne"))
