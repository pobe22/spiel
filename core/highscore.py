import json

def save_score(player_name, score, file="logs/highscores.json"):
    try:
        with open(file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    data.append({"name": player_name, "score": score})
    with open(file, "w") as f:
        json.dump(data, f, indent=2)
