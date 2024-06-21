
# Mehrspieler Quiz

## Inhaltsverzeichnis

- [Über das Projekt](#über-das-projekt)
- [Features](#features)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Projektstruktur](#projektstruktur)
- [Fragensätze](#fragensätze)
- [Autoren](#autoren)

## Über das Projekt

Mehrspieler Quiz ist ein unterhaltsames und interaktives Quiz-Spiel, das es Spielern ermöglicht, lokal in einem Netzwerk gegeneinander anzutreten. Die Spieler können Fragen aus verschiedenen Datensätzen beantworten und Punkte basierend auf der Geschwindigkeit ihrer Antworten sammeln.

## Features

- Mehrspieler-Modus: Erstelle oder trete einem Quiz-Spiel bei.
- Verschiedene Fragendatensätze (z.B., DTSM, INF).
- Punktesystem, bei dem Punkte für schnelle und richtige Antworten vergeben werden.
- Anzeige des Punktestands nach jeder Frage.
- Timer für jede Frage, um die Antwortzeit zu begrenzen.

## Voraussetzungen

- Python 3.x
- `tkinter` Bibliothek (normalerweise mit Python vorinstalliert)

## Installation

1. **Repository klonen**:
   ```bash
   git clone https://github.com/deinbenutzername/mehrspieler-quiz.git
   cd mehrspieler-quiz
   ```

2. **Abhängigkeiten installieren**:
   Es gibt keine zusätzlichen Abhängigkeiten außer `tkinter`, das normalerweise mit Python vorinstalliert ist.

3. **Fragensätze vorbereiten**:
   Erstelle eine Datei `questions.py` und definiere deine Fragendatensätze dort. Zum Beispiel:

   ```python
   questionsDTSM = {
       "Was ist die Hauptstadt von Deutschland?": {"a": "Berlin", "b": "München", "c": "Hamburg", "correct": "a"},
       "Welches Jahr war der Beginn des Zweiten Weltkriegs?": {"a": "1939", "b": "1945", "c": "1914", "correct": "a"},
       # Weitere Fragen...
   }

   questionsINF = {
       "Was bedeutet HTML?": {"a": "HyperText Markup Language", "b": "HyperText Makeup Language", "c": "Hyperlink and Text Markup Language", "correct": "a"},
       "Wer hat das World Wide Web erfunden?": {"a": "Bill Gates", "b": "Tim Berners-Lee", "c": "Steve Jobs", "correct": "b"},
       # Weitere Fragen...
   }
   ```

## Verwendung

1. **Quiz starten**:
   ```bash
   python multiplayerquizapp.py
   ```
2. Wähle "Spiel erstellen" oder "Spiel beitreten", um das Quiz zu starten.

## Projektstruktur

```
mehrspieler-quiz/
├── multiplayerquizapp.py
├── questions.py
├── README.md
```

## Fragensätze

Die Fragensätze sind in der Datei `questions.py` definiert und können leicht angepasst oder erweitert werden.

## Autoren

- [pobe22](https://github.com/pobe)

