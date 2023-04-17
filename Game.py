class Game:
    def __init__(self, term):
        self.term = term
        self.teams = []
        self.result = None

    def add_team(self, team):
        self.teams.append(team)

    def play_game(self):
        if len(self.teams) != 2:
            print("A game must have 2 teams to play.")
            return
        team_a_avg_credit = self.teams[0].get_average_credit()
        team_b_avg_credit = self.teams[1].get_average_credit()
        if team_a_avg_credit > team_b_avg_credit:
            self.result = (self.teams[0], self.teams[1])
        else:
            self.result = (self.teams[1], self.teams[0])


class Round:
    def __init__(self, round_number):
        self.round_number = round_number
        self.games = []

    def add_game(self, game):
        self.games.append(game)
