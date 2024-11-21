import tkinter as tk

def count_words():
    text = text_area.get("1.0", "end-1c")
    word_count = len(text.split())
    result_label.config(text=f"Word Count: {word_count}")

window = tk.Tk()
window.title("Word Counter")

text_area = tk.Text(window, wrap=tk.WORD)
text_area.pack(expand=True, fill="both")

count_button = tk.Button(window, text="Count Words", command=count_words)
count_button.pack()

result_label = tk.Label(window, text="Word Count: 0")
result_label.pack()

window.mainloop()