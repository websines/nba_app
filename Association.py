from Teams import Teams
from Player import Player
from Season import Season

class Association:
    def __init__(self):
        self.teams = Teams()
        self.seasons = []

         # Adding default teams
        suns = self.teams.create_team("Suns")
        bulls = self.teams.create_team("Bulls")
        hawks = self.teams.create_team("Hawks")
        nets = self.teams.create_team("Nets")

        # # Adding players to the Suns
        suns.add_player(Player("Devin Booker", credit=2500, number=1, age=26))
        suns.add_player(Player("Chris Paul", 1500, 3, 37))
        suns.add_player(Player("Deandre Ayton", 2000, 22, 24))
        suns.add_player(Player("Kevin Durant", 3000, 35, 34))
        suns.add_player(Player("Terrence Ross", 1000, 8, 32))

        # # # Adding players to the Bulls
        bulls.add_player(Player("Andre Drummond", 1500, 3, 29))
        bulls.add_player(Player("Zach LaVine", 3000, 8, 28))
        bulls.add_player(Player("Dalen Terry", 900, 25, 20))
        bulls.add_player(Player("Terry Taylor", 1000, 32, 23))
        bulls.add_player(Player("Carlik Jones", 800, 22, 25))

        # # # Adding players to the Hawks
        hawks.add_player(Player("Trae Young", 2200, 11, 24))
        hawks.add_player(Player("John Collins", 2000, 20, 25))
        hawks.add_player(Player("Aaron Holiday", 800, 3, 26))
        hawks.add_player(Player("Jalen Johnson", 1000, 1, 21))
        hawks.add_player(Player("Trent Forrest", 1200, 2, 24))

        # # # Adding players to the Nets
        nets.add_player(Player("Mikal Bridges", 2400, 1, 26))
        nets.add_player(Player("Ben Simmons", 2000, 10, 26))
        nets.add_player(Player("Patty Mills", 900, 8, 34))
        nets.add_player(Player("Joe Harris", 1200, 12, 31))
        nets.add_player(Player("Seth Curry", 1900, 3, 32))

    def display_menu(self):
        print("Welcome to the Association!")
        print("Please make a selection from the menu:")
        print("1. Explore the teams.")
        print("2. Arrange a new season.")
        print("X. Exit the system.")

    def explore_teams(self):
        self.teams.manage_teams()

    def arrange_season(self):
        team_list = self.teams.get_teams_list()
        season = Season(team_list)
        season.display_menu()

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter a choice: ")
            
            if choice == "1":
                self.explore_teams()
            elif choice == "2":
                self.arrange_season()
            elif choice.upper() == "X":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    association = Association()
    association.run()
