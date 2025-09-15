class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        """Erhöhe den Punktestand um die übergebene Zahl."""
        self.score += points

    def reset_score(self):
        """Setze den Punktestand auf 0 zurück."""
        self.score = 0

    def __str__(self):
        return f"{self.name}: {self.score} Punkte"
