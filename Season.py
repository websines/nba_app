from Record import Record

class Season:
    def __init__(self, team_list):
        self.teams = team_list
        self.round = []
        self.game_results = []
        self.term = 0
        self.round_number = 1

    def display_menu(self):
        print("Welcome to the season page! Please make a selection from the menu:")
        print("1. Add a team to the round.")
        print("2. Display the current round.")
        print("3. Play games.")
        print("4. Display the game result records.")
        print("R. Return to previous menu.")
        choice = input("Enter a choice: ")
        while choice.upper() != "R":
            if choice == "1":
                self.add_team_to_round()
            elif choice == "2":
                self.display_current_round()
            elif choice == "3":
                self.play_games()
            elif choice == "4":
                self.display_game_records()
            else:
                print("Invalid choice. Please try again.")
            print("\n")
            print("Welcome to the season page! Please make a selection from the menu:")
            print("1. Add a team to the round.")
            print("2. Display the current round.")
            print("3. Play games.")
            print("4. Display the game result records.")
            print("R. Return to previous menu.")
            choice = input("Enter a choice: ")

    def add_team_to_round(self):
        print("The existing teams are as follows:")
        for team in self.teams:
            print(team.get_team_name())
        team_name = input("Please enter the team's name that you want to schedule: ")
        team = self.find_team_by_name(team_name)
        if team:
            self.round.append(team)
            print(f"Team {team.get_team_name()} has been added at the Game {len(self.round)//2} position {len(self.round) % 2}")
            self.teams.remove(team)
        else:
            print("No such team! Please try again")

    def find_team_by_name(self, team_name):
        for team in self.teams:
            if team.get_team_name() == team_name:
                return team
        return None

    def display_current_round(self):
        print("+-------------------+------+-------------------+")
        print("| First Team        |      | Second Team       |")
        print("+-------------------+------+-------------------+")
        for i in range(0, len(self.round), 2):
            print("| {:<17} |  vs  | {:<17} |".format(self.round[i].get_team_name(), self.round[i + 1].get_team_name()))
        print("+-------------------+------+-------------------+")

    def play_games(self):
        for i in range(0, len(self.round), 2):
            first_team = self.round[i]
            second_team = self.round[i + 1]
            if first_team.get_average_credit() > second_team.get_average_credit():
                winner, loser = first_team, second_team
            else:
                winner, loser = second_team, first_team

            self.game_results.append(Record(winner.get_team_name(), loser.get_team_name(), len(self.game_results) + 1, self.round_number))

            # Update players' credits based on the game result
            credit_difference = abs(first_team.get_average_credit() - second_team.get_average_credit())
            winner.update_credits(credit_difference)
            loser.update_credits(-credit_difference)
        self.round_number += 1
        self.term += 1

    def display_game_records(self):
        print("+------------+------------+---------+------------+")
        print("| Winning Team | Losing Team | Game No. | Round No. |")
        print("+------------+------------+---------+------------+")
        for record in self.game_results:
            print("| {:<12} | {:<12} | {:<7} | {:<10} |".format(record.win_team, record.lose_team, record.game_no, record.round_number))
        print("+------------+------------+---------+------------+")
