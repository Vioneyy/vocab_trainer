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

        self.label_word = tk.Label(root, text="", font=("Arial", 24))
        self.label_word.pack(pady=20)

        self.entry_answer = tk.Entry(root, font=("Arial", 16))
        self.entry_answer.pack()

        self.button_check = tk.Button(root, text="✅ ตรวจคำตอบ", command=self.check_answer)
        self.button_check.pack(pady=5)

        self.label_result = tk.Label(root, text="", font=("Arial", 14))
        self.label_result.pack()

        self.button_next = tk.Button(root, text="➡️ คำถัดไป", command=self.next_word)
        self.button_next.pack(pady=5)

        self.label_score = tk.Label(root, text="คะแนน: 0", font=("Arial", 12))
        self.label_score.pack(pady=5)

        self.next_word()

    def next_word(self):
        self.word = random.choice(vocab_list)
        self.label_word.config(text=self.word['english'])
        self.entry_answer.delete(0, tk.END)
        self.label_result.config(text="")

    def check_answer(self):
        answer = self.entry_answer.get().strip()
        if answer == self.word['thai']:
            self.label_result.config(text="✅ ถูกต้อง!", fg="green")
            self.score += 1
        else:
            self.label_result.config(text=f"❌ ผิด คำแปลคือ: {self.word['thai']}", fg="red")
        self.label_score.config(text=f"คะแนน: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VocabApp(root)
    root.mainloop()
