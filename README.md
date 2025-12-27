Language_Translator

A simple English ↔ Nepali translator with a popup GUI built in Tkinter.
Works online via Google Translate (through deep-translator) and is threaded so the GUI never freezes.

Features

Translate English → Nepali and Nepali → English.

Threaded GUI to prevent freezing during translation.

Copy output to clipboard with one click.

Clear input easily.

Lightweight and portable; works on Windows, Linux, and macOS.

Setup

(Optional) Create a virtual environment:

python -m venv .venv


Activate it:

Windows:

.venv\Scripts\activate


Linux / macOS:

source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt


requirements.txt:

tk
deep-translator

Running the GUI
python Translator_main.py


Enter text in the input box.

Choose the translation direction (English → Nepali or Nepali → English).

Click Translate.

Copy output with Copy Output, or clear input with Clear.