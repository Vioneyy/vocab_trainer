import tkinter as tk
import random
from vocab_data import vocab_list

class VocabApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 โปรแกรมฝึกคำศัพท์ภาษาอังกฤษ")
        self.root.geometry("400x300")

        self.word = {}
        self.score = 0
        self.answered = False 

        self.label_word = tk.Label(root, text="", font=("Arial", 24))
        self.label_word.pack(pady=20)

        self.entry_answer = tk.Entry(root, font=("Arial", 16))
        self.entry_answer.pack()

        self.button_check = tk.Button(root, text="✅ ตรวจคำตอบ", command=self.check_answer)
        self.button_check.pack(pady=5)

        self.label_result = tk.Label(root, text="", font=("Arial", 14))
        self.label_result.pack()

        self.label_score = tk.Label(root, text="คะแนน: 0", font=("Arial", 12))
        self.label_score.pack(pady=5)

        self.next_word()

    def next_word(self):
        self.word = random.choice(vocab_list)
        self.label_word.config(text=self.word['english'])
        self.entry_answer.delete(0, tk.END)
        self.label_result.config(text="")
        self.answered = False 

    def check_answer(self):
        if self.answered:
            return

        answer = self.entry_answer.get().strip()
        if answer == self.word['thai']:
            self.label_result.config(text="✅ ถูกต้อง!", fg="green")
            self.score += 1
            self.label_score.config(text=f"คะแนน: {self.score}")
        else:
            self.label_result.config(text=f"❌ ผิด! คำแปลคือ: {self.word['thai']}", fg="red")

        self.answered = True
        self.root.after(1500, self.next_word) 

if __name__ == "__main__":
    root = tk.Tk()
    app = VocabApp(root)
    root.mainloop()
