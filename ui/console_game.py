from core.game import QuizGame, Player
from data import ALL_QUESTION_SETS
import random

def choose_question_set():
    print("\nVerfügbare Fragensätze:")
    keys = list(ALL_QUESTION_SETS.keys())
    for i, key in enumerate(keys, start=1):
        print(f"{i}. {key}")
    print(f"{len(keys)+1}. Alle Fragensätze zusammen spielen")

    while True:
        try:
            choice = int(input("\nWähle eine Nummer: "))
            if 1 <= choice <= len(keys):
                questions_dict = ALL_QUESTION_SETS[keys[choice-1]]
                # dict in Liste von Fragen umwandeln
                questions_list = []
                for q_text, q_data in questions_dict.items():
                    q_entry = {"question": q_text, **q_data}
                    questions_list.append(q_entry)
                random.shuffle(questions_list)
                return questions_list
            elif choice == len(keys)+1:
                combined = []
                for q_dict in ALL_QUESTION_SETS.values():
                    for q_text, q_data in q_dict.items():
                        q_entry = {"question": q_text, **q_data}
                        combined.append(q_entry)
                random.shuffle(combined)
                return combined
        except ValueError:
            pass
        print("Ungültige Eingabe, bitte nochmal versuchen.")

def play_console_quiz():
    question_set = choose_question_set()
    game = QuizGame(question_set)  # QuizGame muss Liste akzeptieren
    player_name = input("Wie ist dein Name? ")
    player = Player(player_name)

    while game.has_next():
        question = game.get_next_question()  # liefert jetzt ein Dict
        print("\n" + question["question"])
        for key in ["a","b","c"]:
            print(f"{key}: {question[key]}")
        answer = input("Deine Antwort: ")
        if answer.lower() == question["correct"]:
            print("Richtig!")
            player.score += 1
        else:
            print(f"Falsch! Richtige Antwort: {question['correct']}")


    print(f"\n{player.name}, du hast {player.score} Punkte erreicht!")

    # Wiederholung falscher Fragen
    if game.asked_questions:
        retry = input("Möchtest du die falschen Fragen wiederholen? (j/n): ")
        if retry.lower() == 'j':
            game.reset_wrong_questions()
            play_console_quiz()

if __name__ == "__main__":
    play_console_quiz()
