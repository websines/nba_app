from Utils import Utils
class Record:
    def __init__(self, win_team, lose_team, game_no, round_no):
        self.win_team = win_team
        self.lose_team = lose_team
        self.game_no = game_no
        self.round_no = round_no

    def __str__(self):
        return f"{self.round_no} {self.game_no} {self.win_team.name} {self.lose_team.name}"

    def get_data(self):
        return {
            "round_no": self.round_no,
            "game_no": self.game_no,
            "win_team": self.win_team.name,
            "lose_team": self.lose_team.name,
        }
