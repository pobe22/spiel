import tkinter as tk
from tkinter import messagebox
from questions import questionsDTSM, questionsINF
import random

questions = {"DTSM": questionsDTSM, "INF": questionsINF}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("800x600")

        self.question_set = None
        self.questions = []
        self.current_question = 0
        self.correct_answers = 0
        self.asked_questions = []

        self.question_label = tk.Label(root, text="", wraplength=550, justify="left")
        self.question_label.pack(pady=20)

        self.option_a = tk.Button(root, text="", command=lambda: self.check_answer('a'))
        self.option_a.pack(fill=tk.X, padx=20, pady=5)
        self.option_b = tk.Button(root, text="", command=lambda: self.check_answer('b'))
        self.option_b.pack(fill=tk.X, padx=20, pady=5)
        self.option_c = tk.Button(root, text="", command=lambda: self.check_answer('c'))
        self.option_c.pack(fill=tk.X, padx=20, pady=5)

        self.next_button = tk.Button(root, text="Nächste Frage", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=20)

        self.retry_button = tk.Button(root, text="Erneut versuchen", command=self.retry_questions, state=tk.DISABLED)
        self.retry_button.pack(pady=20)

        self.choose_question_set()

    def choose_question_set(self):
        choice = tk.StringVar()
        choice.set("INF")

        def set_choice(value):
            if value in questions:
                self.question_set = questions[value]
                self.start_frame.pack_forget()
                self.choose_question_count()
            else:
                messagebox.showerror("Fehler", "Ungültige Auswahl. Bitte wähle 'DTSM' oder 'INF'.")

        self.start_frame = tk.Frame(self.root)
        self.start_frame.pack(pady=20)

        tk.Label(self.start_frame, text="Welchen Fragendatensatz möchtest du verwenden?").pack()
        tk.Button(self.start_frame, text="DTSM", command=lambda: set_choice("DTSM")).pack(pady=5)
        tk.Button(self.start_frame, text="INF", command=lambda: set_choice("INF")).pack(pady=5)

    def choose_question_count(self):
        def set_count():
            self.question_count = question_slider.get()
            self.count_frame.pack_forget()
            self.start_quiz()

        self.count_frame = tk.Frame(self.root)
        self.count_frame.pack(pady=20)

        tk.Label(self.count_frame, text="Wie viele Fragen möchtest du beantworten?").pack()
        question_slider = tk.Scale(self.count_frame, from_=1, to=len(self.question_set), orient=tk.HORIZONTAL)
        question_slider.set(len(self.question_set))  # Setze den Slider auf die maximale Anzahl von Fragen
        question_slider.pack(pady=5)

        confirm_button = tk.Button(self.count_frame, text="Bestätigen", command=set_count)
        confirm_button.pack(pady=5)


    def start_quiz(self):
        self.questions = list(self.question_set.items())
        random.shuffle(self.questions)
        self.show_question()

    def show_question(self):
        question, options = self.questions[self.current_question]
        self.question_label.config(text=question)
        self.option_a.config(text="a: " + options['a'])
        self.option_b.config(text="b: " + options['b'])
        self.option_c.config(text="c: " + options['c'])
        self.next_button.config(state=tk.DISABLED)

    def check_answer(self, answer):
        question, options = self.questions[self.current_question]
        if answer == options['correct']:
            messagebox.showinfo("Richtig!", "Das ist korrekt!")
            self.correct_answers += 1
        else:
            messagebox.showerror("Falsch", f"Leider falsch. Die richtige Antwort ist: {options['correct']}")
            self.asked_questions.append((question, options))
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        if self.current_question < self.question_count:
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        result_text = f"Du hast {self.correct_answers} von {self.question_count} Fragen richtig beantwortet."
        messagebox.showinfo("Ergebnis", result_text)
        self.retry_button.config(state=tk.NORMAL)

    def retry_questions(self):
        self.current_question = 0
        self.correct_answers = 0
        self.questions = self.asked_questions[:]
        self.asked_questions = []
        random.shuffle(self.questions)
        self.question_count = len(self.questions)
        self.show_question()
        self.retry_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
