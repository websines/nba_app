from Game import Game, Round
from Record import Record

class Season:
    def __init__(self, teams):
        self.available_teams = teams
        self.current_round_games = [Game(i + 1) for i in range(len(teams) // 2)]
        self.current_round = 1
        self.current_round_winners = []
        self.result_records = []

    def get_team_by_name(self, team_name):
        for team in self.available_teams:
            if team.name == team_name:
                return team
        return None

    def find_or_create_game_for_round(self):
        for game in self.current_round_games:
            if not game.is_full():
                return game

        new_game = Game(len(self.current_round_games) + 1)
        self.current_round_games.append(new_game)
        return new_game

    def add_team_to_round(self):
        print("The existing teams are as follows:")
        for team in self.available_teams:
            print(team.name)

        team_name = input("Please enter the team's name that you want to schedule: ")

        team = self.get_team_by_name(team_name)
        if not team:
            print("No such team! Please try again.")
            return

        game = self.find_or_create_game_for_round()
        game.add_team(team)

        self.available_teams.remove(team)
        print(f"Team {team.name} has been added at the Game {game.term} position {len(game.teams)}")

    def display_current_round(self):
        print(f"\nCurrent Round: {self.current_round}")
        print("+-------+------+----------------+----------------+")
        print("| Game  | Team 1            | Team 2          |")
        print("+-------+------+----------------+----------------+")
        for game in self.current_round_games:
            print("| {0:5d} | {1:16s} | {2:16s} |".format(game.term, game.team1.name if game.team1 else '', game.team2.name if game.team2 else ''))
        print("+-------+------+----------------+----------------+")

    def play_games(self):
        if not self.all_games_filled():
            print("Not all games are filled yet. Please add all teams to games.")
            return

        self.play_current_round_games()
        if self.is_season_end():
            print(f"Season winner: {self.current_round_winners[0].name}")
        else:
            self.update_teams_for_next_round()

    def display_game_results(self):
        print("\nGame Result Records:")
        print("+-------+------+--------------+--------------+")
        print("| Round | Game | Winning Team | Losing Team  |")
        print("+-------+------+--------------+--------------+")
        for record in self.result_records:
            print("| {0:5d} | {1:4d} | {2:12s} | {3:12s} |".format(record.round, record.game, record.winner, record.loser))
        print("+-------+------+--------------+--------------+")

    def display_menu(self):
        while True:
            print("\nWelcome to the season page! Please make a selection from the menu:")
            print("1. Add a team to the round.")
            print("2. Display the current round.")
            print("3. Play games.")
            print("4. Display the game result records.")
            print("R. Return to previous menu.")
            choice = input("Enter a choice: ").strip()

            if choice == '1':
                self.add_team_to_round()
            elif choice == '2':
                self.display_current_round()
            elif choice == '3':
                self.play_games()
            elif choice == '4':
                self.display_game_results()
            elif choice.upper() == 'R':
                break
            else:
                print("Invalid choice. Please try again.")
