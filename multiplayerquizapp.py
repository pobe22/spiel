import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import socket
from questions import questionsDTSM, questionsINF, questionsCSHARP

questions = {"DTSM": questionsDTSM, "INF": questionsINF, "CSHARP": questionsCSHARP}


class MultiplayerQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mehrspieler Quiz")
        self.root.geometry("800x600")

        self.current_screen = "main"
        self.question_set = None
        self.questions = []
        self.current_question = 0
        self.correct_answers = 0
        self.asked_questions = []
        self.game_code = None
        self.server = None
        self.client = None
        self.conn = None  
        self.addr = None
        self.server_thread = None
        self.client_thread = None

        self.question_label = tk.Label(self.root, text="", wraplength=550, justify="left")
        self.option_a = tk.Button(self.root, text="", command=lambda: self.check_answer('a'))
        self.option_b = tk.Button(self.root, text="", command=lambda: self.check_answer('b'))
        self.option_c = tk.Button(self.root, text="", command=lambda: self.check_answer('c'))
        self.next_button = tk.Button(self.root, text="Nächste Frage", command=self.next_question, state=tk.DISABLED)
        self.retry_button = tk.Button(self.root, text="Erneut versuchen", command=self.retry_questions, state=tk.DISABLED)
        
        self.result_label = tk.Label(root, text="")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.create_main_screen()

    def create_main_screen(self):
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        tk.Label(self.main_frame, text="Mehrspieler Quiz", font=("Helvetica", 18)).pack(pady=20)

        tk.Button(self.main_frame, text="Spiel erstellen", command=self.create_game_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Spiel beitreten", command=self.join_game_screen).pack(pady=10)

    def create_game_screen(self):
        self.current_screen = "create"
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        tk.Label(self.main_frame, text="Spiel erstellen", font=("Helvetica", 18)).pack(pady=20)

        self.game_code_label = tk.Label(self.main_frame, text="Spielcode: ")
        self.game_code_label.pack()

        self.create_button_dtsm = tk.Button(self.main_frame, text="DTSM", command=lambda: self.create_game("DTSM"))
        self.create_button_dtsm.pack(pady=5)

        self.create_button_inf = tk.Button(self.main_frame, text="INF", command=lambda: self.create_game("INF"))
        self.create_button_inf.pack(pady=5)
        
        self.create_button_csharp = tk.Button(self.main_frame, text="CSHARP", command=lambda: self.create_game("CSHARP"))
        self.create_button_csharp.pack(pady=5)

        self.start_game_button = tk.Button(self.main_frame, text="Spiel starten", command=self.start_game, state=tk.DISABLED)
        self.start_game_button.pack(pady=10)

        tk.Button(self.main_frame, text="Zurück", command=self.create_main_screen).pack(pady=10)

    def create_game(self, dataset):
        self.question_set = questions[dataset]
        self.game_code = random.randint(1000, 9999)
        self.game_code_label.config(text=f"Spielcode: {self.game_code}")
        self.start_game_button.config(state=tk.NORMAL)
        self.start_server()  # Server starten

    def join_game_screen(self):
        self.current_screen = "join"
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        tk.Label(self.main_frame, text="Spiel beitreten", font=("Helvetica", 18)).pack(pady=20)

        tk.Label(self.main_frame, text="Spielcode eingeben:").pack()

        self.game_code_entry = tk.Entry(self.main_frame)
        self.game_code_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Spiel beitreten", command=self.join_game).pack(pady=5)
        tk.Button(self.main_frame, text="Zurück", command=self.create_main_screen).pack(pady=10)

    def join_game(self):
        game_code = self.game_code_entry.get()
        if game_code.isdigit():
            self.game_code = int(game_code)
            self.question_set = questions["DTSM"]  # Beispielhaft DTSM verwendet
            messagebox.showinfo("Erfolgreich", f"Du bist dem Spiel mit dem Code {self.game_code} beigetreten.")
            self.start_game_button.config(state=tk.NORMAL)
            self.start_client()  # Client starten
        else:
            messagebox.showerror("Fehler", "Ungültiger Spielcode. Bitte geben Sie eine Zahlenkombination ein.")
    
    def start_server(self):
        def server_thread():
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(('0.0.0.0', self.game_code))
            self.server.listen(1)
            self.conn, self.addr = self.server.accept()
            self.receive_data()

        self.server_thread = threading.Thread(target=server_thread)
        self.server_thread.start()

    def start_client(self):
        def client_thread():
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(('localhost', self.game_code))
            self.receive_data()

        self.client_thread = threading.Thread(target=client_thread)
        self.client_thread.start()

    def receive_data(self):
            conn = self.conn if self.conn else self.client
            while True:
                try:
                    data = conn.recv(1024).decode('utf-8')
                    if data:
                        print("Received:", data)
                except Exception as e:
                    print("Error receiving data:", e)
                    break

    def send_data(self, data):
        conn = self.conn if self.conn else self.client
        try:
            conn.sendall(data.encode('utf-8'))
        except Exception as e:
            print("Error sending data:", e)

    def start_game(self):
        self.main_frame.destroy()
        self.current_screen = "game"
        self.load_questions()
        self.start_timer() 
        self.create_quiz_screen()

    def load_questions(self):
        # Hier laden Sie die Fragen basierend auf dem ausgewählten Fragendatensatz
        self.questions = list(self.question_set.items())
        random.shuffle(self.questions)
        self.current_question = 0
        self.correct_answers = 0

    def create_quiz_screen(self):
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        # Anzeigen der Frage
        question, options = self.questions[self.current_question]

        # Frage-Label
        self.question_label = tk.Label(self.main_frame, text=question, wraplength=550, justify="left")
        self.question_label.pack(pady=20)

        # Antwort-Buttons
        self.option_a = tk.Button(self.main_frame, text="a: " + options['a'], command=lambda: self.check_answer('a'))
        self.option_a.pack(fill=tk.X, padx=20, pady=5)
        self.option_b = tk.Button(self.main_frame, text="b: " + options['b'], command=lambda: self.check_answer('b'))
        self.option_b.pack(fill=tk.X, padx=20, pady=5)
        self.option_c = tk.Button(self.main_frame, text="c: " + options['c'], command=lambda: self.check_answer('c'))
        self.option_c.pack(fill=tk.X, padx=20, pady=5)

        # Antwortanzeige
        self.answer_label = tk.Label(self.main_frame, text="", fg="green")
        self.answer_label.pack(pady=10)

        # Nächste Frage Button
        self.next_button = tk.Button(self.main_frame, text="Nächste Frage", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=20)
        
        # Timer-Label
        self.timer_label = tk.Label(self.main_frame, text=f"Restliche Zeit: {self.answer_time} Sekunden")
        self.timer_label.pack(pady=10)

        # Punktestand
        self.score_label = tk.Label(self.main_frame, text="Punktestand: 0")
        self.score_label.pack(pady=10)

    def start_timer(self):
        self.answer_time = 30
        threading.Thread(target=self.timer_thread).start()

    def timer_thread(self):
        while self.answer_time > 0:
            time.sleep(1)
            self.answer_time -= 1
            self.timer_label.config(text=f"Restliche Zeit: {self.answer_time} Sekunden")
            if self.answer_time == 0:
                self.next_button.config(state=tk.NORMAL)

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
            # Berechnung der Punkte für diese Frage
            points_for_question = self.answer_time
            
            # Punktestand erhöhen
            self.correct_answers += points_for_question
            
            # Punktestand anzeigen und speichern
            self.score_label.config(text=f"Punktestand: {self.correct_answers}")
            
            # Antwortlabel aktualisieren
            self.answer_label.config(text=f"Richtig! Du hast {points_for_question} Punkte erhalten.", fg="green")
        else:
            self.answer_label.config(text=f"Falsch. Die richtige Antwort ist: {options['correct']}", fg="red")
            self.asked_questions.append((question, options))
    
        # Nächsten Frage Button aktivieren
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_next_question()
        else:
            self.show_result()
    
    def load_next_question(self):
        self.show_question()
        self.start_timer()

    def show_result(self):
        result_text = f"Du hast {self.correct_answers} von {len(self.questions)} Fragen richtig beantwortet."
        messagebox.showinfo("Ergebnis", result_text)
        self.retry_button.config(state=tk.NORMAL)

    def retry_questions(self):
        self.current_question = 0
        self.correct_answers = 0
        self.questions = self.asked_questions[:]
        self.asked_questions = []
        random.shuffle(self.questions)
        self.show_question()
        self.retry_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiplayerQuizApp(root)
    root.mainloop()
