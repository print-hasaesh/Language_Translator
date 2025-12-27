"""
translator_ui.py
Tkinter GUI for English ↔ Nepali translation using translator_engine.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import translator_engine


def do_translate(text_widget, out_widget, direction_var, status_label, btn):
    txt = text_widget.get("1.0", tk.END).strip()
    if not txt:
        messagebox.showinfo("Empty", "Please enter text to translate.")
        return

    direction = direction_var.get()

    btn.config(state=tk.DISABLED)
    status_label.config(text="Translating…")

    def worker():
        try:
            out = translator_engine.translate(txt, direction)
        except Exception as e:
            out = f"[error] {type(e).__name__}: {e}"

        def update_ui():
            out_widget.config(state=tk.NORMAL)
            out_widget.delete("1.0", tk.END)
            out_widget.insert(tk.END, out)
            out_widget.config(state=tk.DISABLED)
            status_label.config(text="Done")
            btn.config(state=tk.NORMAL)

        text_widget.after(0, update_ui)

    threading.Thread(target=worker, daemon=True).start()


def build_ui():
    root = tk.Tk()
    root.title("Translator — English ↔ Nepali")
    root.geometry("600x440")
    root.resizable(False, False)

    frm = ttk.Frame(root, padding=10)
    frm.pack(fill=tk.BOTH, expand=True)

    # Direction
    direction_var = tk.StringVar(value="en-ne")
    dir_frame = ttk.Frame(frm)
    dir_frame.pack(fill=tk.X)
    ttk.Label(dir_frame, text="Direction:").pack(side=tk.LEFT)
    ttk.Radiobutton(dir_frame, text="English → Nepali", variable=direction_var, value="en-ne").pack(side=tk.LEFT, padx=6)
    ttk.Radiobutton(dir_frame, text="Nepali → English", variable=direction_var, value="ne-en").pack(side=tk.LEFT, padx=6)

    # Input
    ttk.Label(frm, text="Input:").pack(anchor=tk.W, pady=(10, 0))
    txt_in = scrolledtext.ScrolledText(frm, height=8, wrap=tk.WORD)
    txt_in.pack(fill=tk.X)

    # Buttons
    btn_frame = ttk.Frame(frm)
    btn_frame.pack(fill=tk.X, pady=8)
    status_label = ttk.Label(btn_frame, text="Idle")
    status_label.pack(side=tk.RIGHT)

    txt_out = scrolledtext.ScrolledText(frm, height=8, state=tk.DISABLED, wrap=tk.WORD)

    translate_btn = ttk.Button(btn_frame, text="Translate",
                               command=lambda: do_translate(txt_in, txt_out, direction_var, status_label, translate_btn))
    translate_btn.pack(side=tk.LEFT)
    ttk.Button(btn_frame, text="Clear", command=lambda: txt_in.delete("1.0", tk.END)).pack(side=tk.LEFT, padx=6)
    ttk.Button(btn_frame, text="Copy Output",
               command=lambda: copy_output(root, txt_out)).pack(side=tk.LEFT, padx=6)

    # Output
    ttk.Label(frm, text="Output:").pack(anchor=tk.W)
    txt_out.pack(fill=tk.BOTH, expand=True)

    return root


def copy_output(root, txt_out):
    out = txt_out.get("1.0", tk.END).strip()
    if out:
        root.clipboard_clear()
        root.clipboard_append(out)
        messagebox.showinfo("Copied", "Translated text copied to clipboard.")


def main():
    root = build_ui()
    root.mainloop()


if __name__ == "__main__":
    main()
