from Team import Team
from Utils import Utils

class Teams:
    def __init__(self):
        self.teams = []

    def create_team(self, team_name):
        team = Team(team_name)
        self.teams.append(team)
        return team
    
    def find_team_by_name(self, name):
        for team in self.teams:
            if team.get_name() == name:
                return team
        return None
    
    def get_teams_list(self):
        return self.teams

    def remove_team(self, team_name):
        team = self.get_team_by_name(team_name)
        if team:
            self.teams.remove(team)
            return True
        return False

    def get_team_by_name(self, team_name):
        for team in self.teams:
            if team.get_team_name() == team_name:
                return team
        return None

    def get_all_teams(self):
        return self.teams

    def manage_teams(self):
        print("Welcome to the Teams Page!")
        print("Please make a selection from the menu:")
        print("1. Display all teams.")
        print("2. Display all players.")
        print("3. Add a new team.")
        print("4. Manage an existing team.")
        print("5. Delete an existing team.")
        print("6. Display all players by level.")
        print("R. Return to previous menu.")
        choice = input("Enter a choice: ")
        while choice.upper() != "R":
            if choice == "1":
                self.display_all_teams()
            elif choice == "2":
                self.display_all_players()
            elif choice == "3":
                self.add_new_team()
            elif choice == "4":
                self.manage_existing_team()
            elif choice == "5":
                self.delete_existing_team()
            elif choice == "6":
                self.display_all_players_by_level()
            else:
                print("Invalid choice. Please try again.")
            print("\n")
            print("Welcome to the Teams Page!")
            print("Please make a selection from the menu:")
            print("1. Display all teams.")
            print("2. Display all players.")
            print("3. Add a new team.")
            print("4. Manage an existing team.")
            print("5. Delete an existing team.")
            print("6. Display all players by level.")
            print("R. Return to previous menu.")
            choice = input("Enter a choice: ")

    def display_all_teams(self):
        print("Displaying all teams:")
        Utils.teamsHeader()
        for team in self.teams:
            print(Utils.teamsFormat(team.get_team_name(), team.get_num_players(), team.get_average_credit(), team.get_average_age()))
        Utils.teamTableEnd()

    def display_all_players(self):
        print("Displaying all players:")
        for team in self.teams:
            print(f"Team Name: {team.get_team_name()}")
            team.display_team_players()
            print("\n")

    def add_new_team(self):
        team_name = input("Enter the name of the new team: ")
        self.create_team(team_name)
        print(f"Created team: {team_name}")

    def manage_existing_team(self):
        team_name = input("Enter the name of the team you want to manage: ")
        team = self.get_team_by_name(team_name)
        if team is not None:
            team.manage_team()
        else:
            print("Team not found. Please try again.")

    def delete_existing_team(self):
        team_name = input("Enter the name of the team you want to delete: ")
        if self.remove_team(team_name):
            print(f"Team deleted: {team_name}")
        else:
            print("Team not found. Please try again.")

    def display_all_players_by_level(self):
        level = input("Enter the level of players you want to display: ")
        for team in self.teams:
            print(f"Team Name: {team.get_team_name()}")
            team.display_players_by_level(level)
            print("\n")