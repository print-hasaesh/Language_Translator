# Language_Translator

Simple English ↔ Nepali translator with a popup GUI.

Setup
-----

1. (Optional) Create a virtualenv, then install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the GUI:

```bash
python Translator_main.py
```

Notes
-----
- The translator uses `googletrans` when available and falls back to a tiny built-in dictionary otherwise.
- If you don't want to install `googletrans`, the fallback still translates a few common phrases.
Check 