"""Simple GUI popup to translate between English and Nepali.

Run this file to open a small window for translation.
"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

import translator_engine


def do_translate(text_widget, out_widget, direction_var):
	txt = text_widget.get("1.0", tk.END).strip()
	if not txt:
		messagebox.showinfo("Empty", "Please enter text to translate.")
		return
	direction = direction_var.get()
	out = translator_engine.translate(txt, direction)
	out_widget.config(state=tk.NORMAL)
	out_widget.delete("1.0", tk.END)
	out_widget.insert(tk.END, out)
	out_widget.config(state=tk.DISABLED)


def build_ui():
	root = tk.Tk()
	root.title("Translator — English <> Nepali")
	root.geometry("600x420")

	frm = ttk.Frame(root, padding=10)
	frm.pack(fill=tk.BOTH, expand=True)

	direction_var = tk.StringVar(value="en-ne")
	dir_frame = ttk.Frame(frm)
	dir_frame.pack(fill=tk.X)
	ttk.Label(dir_frame, text="Direction:").pack(side=tk.LEFT)
	ttk.Radiobutton(dir_frame, text="English → Nepali", variable=direction_var, value="en-ne").pack(side=tk.LEFT, padx=6)
	ttk.Radiobutton(dir_frame, text="Nepali → English", variable=direction_var, value="ne-en").pack(side=tk.LEFT, padx=6)

	ttk.Label(frm, text="Input:").pack(anchor=tk.W, pady=(8, 0))
	txt_in = scrolledtext.ScrolledText(frm, height=8)
	txt_in.pack(fill=tk.BOTH, expand=False)

	btn_frame = ttk.Frame(frm)
	btn_frame.pack(fill=tk.X, pady=8)
	translate_btn = ttk.Button(btn_frame, text="Translate", command=lambda: do_translate(txt_in, txt_out, direction_var))
	translate_btn.pack(side=tk.LEFT)
	clear_btn = ttk.Button(btn_frame, text="Clear", command=lambda: txt_in.delete("1.0", tk.END))
	clear_btn.pack(side=tk.LEFT, padx=6)

	ttk.Label(frm, text="Output:").pack(anchor=tk.W)
	txt_out = scrolledtext.ScrolledText(frm, height=8, state=tk.DISABLED)
	txt_out.pack(fill=tk.BOTH, expand=True)

	def copy_output():
		out = txt_out.get("1.0", tk.END).strip()
		if out:
			root.clipboard_clear()
			root.clipboard_append(out)
			messagebox.showinfo("Copied", "Translated text copied to clipboard.")

	copy_btn = ttk.Button(btn_frame, text="Copy Output", command=copy_output)
	copy_btn.pack(side=tk.RIGHT)

	return root


def main():
	root = build_ui()
	root.mainloop()


if __name__ == "__main__":
	main()
