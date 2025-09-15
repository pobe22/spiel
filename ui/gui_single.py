import tkinter as tk
from tkinter import messagebox
from core.game import QuizGame, Player
from data import questions_dtsm

class SinglePlayerQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Singleplayer")
        self.player = None

        self.question_set = questions_dtsm.questions2ADAC_DTSM
        self.game = QuizGame(self.question_set)

        self.question_label = tk.Label(root, text="", wraplength=500, justify="left")
        self.question_label.pack(pady=20)

        self.buttons = {}
        for option in ['a', 'b', 'c']:
            btn = tk.Button(root, text="", command=lambda o=option: self.check_answer(o))
            btn.pack(fill=tk.X, padx=20, pady=5)
            self.buttons[option] = btn

        self.score_label = tk.Label(root, text="Punktestand: 0")
        self.score_label.pack(pady=10)

        self.next_button = tk.Button(root, text="Nächste Frage", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=20)

        self.player = Player("Spieler")
        self.show_question()

    def show_question(self):
        question, options = self.game.get_next_question()
        if question is None:
            messagebox.showinfo("Ende", f"Spiel beendet! Dein Punktestand: {self.player.score}")
            self.root.quit()
            return
        self.current_question = question
        self.current_options = options
        self.question_label.config(text=question)
        for key in ['a', 'b', 'c']:
            self.buttons[key].config(text=f"{key}: {options[key]}", state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def check_answer(self, selected):
        correct = self.current_options['correct']
        if selected.lower() == correct.lower():
            self.player.score += 1
            messagebox.showinfo("Richtig!", f"Richtig! Punktestand: {self.player.score}")
        else:
            messagebox.showinfo("Falsch!", f"Falsch! Richtige Antwort: {correct}")
            self.game.asked_questions.append((self.current_question, self.current_options))
        for btn in self.buttons.values():
            btn.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        self.score_label.config(text=f"Punktestand: {self.player.score}")

    def next_question(self):
        self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = SinglePlayerQuizApp(root)
    root.mainloop()
