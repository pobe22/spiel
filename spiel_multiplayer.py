import tkinter as tk
import random
from tkinter import messagebox
import questions
import threading
import time
import random

class MultiplayerLobby:
    def __init__(self, root):
        self.root = root
        self.root.title("Mehrspielerlobby")
        self.root.geometry("400x200")

        self.create_button = tk.Button(root, text="Spiel erstellen", command=self.create_game)
        self.create_button.pack(pady=10)

        self.join_button = tk.Button(root, text="Spiel beitreten", command=self.join_game)
        self.join_button.pack(pady=10)

        self.game_code = None
        self.current_question = None
        self.answer_time = None
        self.questions = None

    def create_game(self):
        self.game_code = random.randint(1000, 9999)  
        print("Spiel erstellen mit dem Spielcode:", self.game_code)
        self.questions = questions.questionsDTSM if self.choose_dataset() == "DTSM" else questions.questionsINF
        self.start_game()

    def join_game(self):
        game_code = input("Bitte gib den Spielcode ein, um dem Spiel beizutreten: ")
        if game_code == str(self.game_code):
            print("Erfolgreich dem Spiel beigetreten!")
            self.questions = questions.questionsDTSM if self.choose_dataset() == "DTSM" else questions.questionsINF
            self.start_game()
        else:
            print("Ungültiger Spielcode. Bitte versuche es erneut.")

    def choose_dataset(self):
        return input("Welchen Fragendatensatz möchtest du verwenden? (DTSM/INF): ").upper()

    def start_game(self):
        # Spiel starten, erste Frage empfangen und anzeigen
        self.receive_question()

    def send_question(self):
        question = random.choice(list(self.questions.keys()))
        self.current_question = question
        self.questions.pop(question)  # Entferne die Frage aus dem Fragenpool
        print("Frage gesendet:", question)

    def receive_question(self):
        question = random.choice(list(self.questions.keys()))
        self.current_question = question
        self.questions.pop(question)  # Entferne die Frage aus dem Fragenpool
        print("Frage empfangen:", question)
        self.start_timer()

    def start_timer(self):
       self.answer_time = 15
       threading.Thread(target=self.timer_thread).start()
       
    def timer_thread(self):
        while self.answer_time > 0:
            time.sleep(1)
            self.answer_time -= 1

    def check_answer(self, answer):
       correct_answer = self.questions[self.current_question]['correct']
       if answer == correct_answer:
           print("Richtig! Du erhältst Punkte.")
           # Hier könntest du Punkte vergeben
       else:
           print("Falsch! Keine Punkte.")
           # Hier könntest du die richtige Antwort anzeigen

    def show_result(self):
        # Endergebnis anzeigen
        print("Spiel beendet. Endergebnis anzeigen...")
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiplayerLobby(root)
    root.mainloop()
