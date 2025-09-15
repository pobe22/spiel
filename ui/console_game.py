from core.game import QuizGame, Player
from data import questions_dtsm  # Beispielhafte Daten

def choose_question_set():
    # Hier kannst du weitere Datensätze einbauen
    return questions_dtsm.questions2ADAC_DTSM

def play_console_quiz():
    question_set = choose_question_set()
    game = QuizGame(question_set)
    player_name = input("Wie ist dein Name? ")
    player = Player(player_name)

    while game.has_next():
        question, options = game.get_next_question()
        print("\n" + question)
        for key, val in options.items():
            if key != 'correct':
                print(f"{key}: {val}")
        answer = input("Deine Antwort: ")
        if game.check_answer(question, answer):
            print("Richtig!")
            player.score += 1
        else:
            print(f"Falsch! Richtige Antwort: {options['correct']}")

    print(f"\n{player.name}, du hast {player.score} Punkte erreicht!")

    # Wiederholung falscher Fragen
    if game.asked_questions:
        retry = input("Möchtest du die falschen Fragen wiederholen? (j/n): ")
        if retry.lower() == 'j':
            game.reset_wrong_questions()
            play_console_quiz()

if __name__ == "__main__":
    play_console_quiz()
