import random
from questions import questionsDTSM, questionsINF, questionsCSHARP

questions = {"DTSM": questionsDTSM, "INF": questionsINF, "CSHARP": questionsCSHARP}

def choose_question_set():
    user_choice = input("Welchen Fragendatensatz möchtest du verwenden? (DTSM/INF/CSHARP): ").upper()
    if user_choice in questions:
        return questions[user_choice]
    else:
        print("Ungültige Auswahl. Bitte wähle 'DTSM' oder 'INF'.")
        return choose_question_set()

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

def choose_question():
    question_set = choose_question_set()
    return random.choice(list(question_set.items()))

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
    question_set = choose_question_set()
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