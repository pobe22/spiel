import tkinter as tk
from tkinter import messagebox
import threading
import random
import socket
from core.game import QuizGame, Player
from data import questions_dtsm, questions_inf

# Verfügbare Datensätze
QUESTION_SETS = {
    "DTSM": questions_dtsm.questions2ADAC_DTSM,
    "INF": questions_inf.questions2ADAC_INF,
}

class MultiplayerQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mehrspieler Quiz")
        self.root.geometry("800x600")

        self.player = Player("Spieler")
        self.game = None
        self.question_set = None
        self.current_question = None
        self.correct_answers = 0
        self.asked_questions = []

        # Netzwerk
        self.server = None
        self.client = None
        self.conn = None
        self.addr = None
        self.game_code = None

        # UI
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        self.create_main_screen()

    # ---------------- Main Screens ----------------
    def create_main_screen(self):
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        tk.Label(self.main_frame, text="Mehrspieler Quiz", font=("Helvetica", 18)).pack(pady=20)
        tk.Button(self.main_frame, text="Spiel erstellen", command=self.create_game_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Spiel beitreten", command=self.join_game_screen).pack(pady=10)

    def create_game_screen(self):
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        tk.Label(self.main_frame, text="Spiel erstellen", font=("Helvetica", 18)).pack(pady=20)
        self.game_code_label = tk.Label(self.main_frame, text="Spielcode: ")
        self.game_code_label.pack()

        for dataset in QUESTION_SETS.keys():
            tk.Button(self.main_frame, text=dataset, command=lambda d=dataset: self.create_game(d)).pack(pady=5)

        self.start_game_button = tk.Button(self.main_frame, text="Spiel starten", state=tk.DISABLED, command=self.start_game)
        self.start_game_button.pack(pady=10)
        tk.Button(self.main_frame, text="Zurück", command=self.create_main_screen).pack(pady=10)

    def join_game_screen(self):
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        tk.Label(self.main_frame, text="Spiel beitreten", font=("Helvetica", 18)).pack(pady=20)
        tk.Label(self.main_frame, text="Spielcode eingeben:").pack()
        self.game_code_entry = tk.Entry(self.main_frame)
        self.game_code_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Spiel beitreten", command=self.join_game).pack(pady=5)
        tk.Button(self.main_frame, text="Zurück", command=self.create_main_screen).pack(pady=10)

    # ---------------- Game Logic ----------------
    def create_game(self, dataset):
        self.question_set = QUESTION_SETS[dataset]
        self.game = QuizGame(self.question_set)
        self.game_code = random.randint(1000, 9999)
        self.game_code_label.config(text=f"Spielcode: {self.game_code}")
        self.start_game_button.config(state=tk.NORMAL)
        self.start_server()

    def join_game(self):
        code = self.game_code_entry.get()
        if code.isdigit():
            self.game_code = int(code)
            self.question_set = QUESTION_SETS["DTSM"]  # Beispielhaft
            self.game = QuizGame(self.question_set)
            messagebox.showinfo("Erfolgreich", f"Spiel beigetreten: {self.game_code}")
            self.start_game_button.config(state=tk.NORMAL)
            self.start_client()
        else:
            messagebox.showerror("Fehler", "Ungültiger Spielcode")

    # ---------------- Networking ----------------
    def start_server(self):
        def server_thread():
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(('0.0.0.0', self.game_code))
            self.server.listen(1)
            self.conn, self.addr = self.server.accept()
            self.receive_data()
        threading.Thread(target=server_thread, daemon=True).start()

    def start_client(self):
        def client_thread():
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(('localhost', self.game_code))
            self.receive_data()
        threading.Thread(target=client_thread, daemon=True).start()

    def receive_data(self):
        conn = self.conn if self.conn else self.client
        while True:
            try:
                data = conn.recv(1024).decode('utf-8')
                if data:
                    print("Received:", data)
            except Exception as e:
                print("Receive error:", e)
                break

    def send_data(self, data):
        conn = self.conn if self.conn else self.client
        try:
            conn.sendall(data.encode('utf-8'))
        except Exception as e:
            print("Send error:", e)

    # ---------------- Quiz UI ----------------
    def start_game(self):
        self.main_frame.destroy()
        self.show_question()

    def show_question(self):
        question, options = self.game.get_next_question()
        if question is None:
            messagebox.showinfo("Ende", f"Punktestand: {self.player.score}")
            self.root.quit()
            return
        self.current_question = question
        self.current_options = options
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        tk.Label(self.main_frame, text=question, wraplength=500, justify="left").pack(pady=20)
        for key in ['a','b','c']:
            tk.Button(self.main_frame, text=f"{key}: {options[key]}", command=lambda k=key: self.check_answer(k)).pack(fill=tk.X, padx=20, pady=5)

    def check_answer(self, selected):
        correct = self.current_options['correct']
        if selected.lower() == correct.lower():
            self.player.add_score(1)
            messagebox.showinfo("Richtig", f"Punktestand: {self.player.score}")
        else:
            messagebox.showinfo("Falsch", f"Richtige Antwort: {correct}")
            self.game.asked_questions.append((self.current_question, self.current_options))
        self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiplayerQuizApp(root)
    root.mainloop()
