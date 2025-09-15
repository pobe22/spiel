import random
from questions import questions2ADAC_DTSM, questions2ADAC_INF, questions2ADAC_CSHARP, questions2ADAC_AWL, questions3ADAC_DTSM, questions3ADAC_INF, questions3ADAC_ITL

questions_2ADAC = {
    "DTSM": questions2ADAC_DTSM,
    "INF": questions2ADAC_INF,
    "CSHARP": questions2ADAC_CSHARP,
    "AWL": questions2ADAC_AWL
}

questions_3ADAC = {
    "DTSM": questions3ADAC_DTSM,
    "INF": questions3ADAC_INF,
    "ITL": questions3ADAC_ITL,

}

class_question_sets = {
    "2ADAC": questions_2ADAC,
    "3ADAC": questions_3ADAC
}


def choose_class():
    while True:
        user_class = input("Welche Klasse besuchst du? (2ADAC/3ADAC): ").upper()
        if user_class in class_question_sets:
            return user_class
        else:
            print("Ungültige Klasse. Bitte gib '2ADAC' oder '3ADAC' ein.")

def choose_question_set(user_class):
    available_sets = class_question_sets[user_class]
    print(f"Für deine Klasse sind folgende Datensätze verfügbar: {', '.join(available_sets)}")
    while True:
        user_choice = input(f"Welchen Fragendatensatz möchtest du verwenden? ({'/'.join(available_sets)}): ").upper()
        if user_choice in available_sets:
            return available_sets[user_choice] 
        else:
            print(f"Ungültige Auswahl. Bitte wähle einen der verfügbaren Datensätze: {', '.join(available_sets)}.")

def choose_question_count():
    while True:
        try:
            question_count = int(input("Wie viele Fragen möchtest du beantworten? (Ganze Zahl eingeben): "))
            if question_count > 0:
                return question_count
            else:
                print("Bitte gib eine positive Zahl ein.")
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")

def ask_question(question, options):
    print(question)
    print() 
    for option, answer in options.items():
        if option != "correct":
            print(option + ": " + answer)
            print()
    user_answer = input("Bitte wähle eine Antwort (a/b/c): ")
    if user_answer.lower() == options['correct']:
        print("Richtig!")
        print()
        return True
    else:
        print("Leider falsch. Die richtige Antwort ist:", options['correct'])
        print()
        return False

def play_game():
    print("Willkommen beim Quiz!")
    user_class = choose_class()
    question_set = choose_question_set(user_class)
    questions = list(question_set.items())
    random.shuffle(questions)
    correct_answers = 0
    question_count = min(choose_question_count(), len(questions))
    asked_questions = []
    for i in range(question_count):
        question, options = questions[i]
        if ask_question(question, options):
            correct_answers += 1
        else:
            asked_questions.append((question, options))
    print("Du hast {} von {} Fragen richtig beantwortet.".format(correct_answers, question_count))
    while asked_questions:
        retry = input("Möchtest du die falschen Fragen nochmal üben? (j/n): ")
        if retry.lower() == "j":
            for question, options in asked_questions:
                if ask_question(question, options):
                    asked_questions.remove((question, options))
        else:
            break
    if not asked_questions:
        play_again = input("Glückwunsch! Du hast alle Fragen richtig beantwortet. Möchtest du nochmal spielen? (j/n): ")
        if play_again.lower() == "j":
            play_game()
        else:
            input("Drücke Enter, um das Programm zu beenden.")

play_game()