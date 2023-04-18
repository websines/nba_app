from Players import Players
from Utils import Utils
class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = Players()
        self.scheduled = False

    def get_team_name(self):
        return self.team_name
    
    def set_scheduled(self, bool):
        self.scheduled = bool

    def set_team_name(self, team_name):
        self.team_name = team_name

    def display_team_players(self):
        print(f"Players in {self.team_name}:")
        self.players.display_players()

    def display_players_by_level(self, level):
        print(f"Players in {self.team_name} with level {level}:")
        self.players.display_players_by_level(level)

    def add_player(self, player):
        self.players.add_player(player.name, player.credit, player.number, player.age)

    def update_player(self):
        self.players.update_player()
    
    def get_num_players(self):
        return len(self.players.players)

    def get_average_credit(self):
        total_credit = sum([player.get_credit() for player in self.players.players])
        return total_credit / len(self.players.players) if len(self.players.players) > 0 else 0

    def get_average_age(self):
        total_age = sum([player.get_age() for player in self.players.players])
        return total_age / len(self.players.players) if len(self.players.players) > 0 else 0

    def delete_player(self):
        self.players.delete_player()

    def manage_team(self):
        print(f"Welcome to the {self.team_name}'s Page!")
        print("Please make a selection from the menu:")
        print("1. Display team's players.")
        print("2. Add a new player.")
        print("3. Update an existing player.")
        print("4. Delete an existing player.")
        print("R. Return to previous menu.")
        choice = input("Enter a choice: ")
        while choice.upper() != "R":
            if choice == "1":
                self.display_team_players()
            elif choice == "2":
                self.add_player()
            elif choice == "3":
                self.update_player()
            elif choice == "4":
                self.delete_player()
            else:
                print("Invalid choice. Please try again.")
            print("\n")
            print(f"Welcome to the {self.team_name}'s Page!")
            print("Please make a selection from the menu:")
            print("1. Display team's players.")
            print("2. Add a new player.")
            print("3. Update an existing player.")
            print("4. Delete an existing player.")
            print("R. Return to previous menu.")
            choice = input("Enter a choice: ")
    
    def update_credits(self, credit_difference):
        for player in self.players.get_players_list():
            player.credit += credit_difference

    def display_credits(self):
        print(f"Players' credits in {self.team_name}:")
        Utils.playerHeader()
        for player in self.players.get_players_list():
            print(Utils.PlayerFormat(player.get_name(), player.get_credit(), player.get_level(), player.get_number(), player.get_age()))
        Utils.playerTableEnd()
            
