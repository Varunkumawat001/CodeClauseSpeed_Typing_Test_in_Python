import tkinter as tk
import random
import time

class SpeedTypingTest:
    def __init__(self, master):
        self.master = master
        self.word_list = ['apple', 'banana', 'orange', 'grape', 'kiwi']  # Sample word list
        self.current_word = ''
        self.input_text = ''
        self.start_time = 0

        self.word_label = tk.Label(master, font=('Arial', 24), pady=10)
        self.word_label.pack()

        self.input_entry = tk.Entry(master, font=('Arial', 18))
        self.input_entry.pack()

        self.result_label = tk.Label(master, font=('Arial', 18), pady=10)
        self.result_label.pack()

        self.new_word()
        self.input_entry.focus_set()
        self.input_entry.bind('<Return>', self.check_word)

    def new_word(self):
        self.current_word = random.choice(self.word_list)
        self.word_label.config(text=self.current_word)
        self.start_time = time.time()

    def check_word(self, event):
        self.input_text = self.input_entry.get()
        self.input_entry.delete(0, tk.END)

        if self.input_text == self.current_word:
            elapsed_time = time.time() - self.start_time
            self.result_label.config(text=f"WPM {elapsed_time:.2f} seconds")
        else:
            self.result_label.config(text="Incorrect! Try again.")

        self.new_word()

root = tk.Tk()
root.title("Speed Typing Test")
app = SpeedTypingTest(root)
root.mainloop()
