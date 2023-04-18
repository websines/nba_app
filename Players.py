from Utils import Utils
from Player import Player
class Players:
    def __init__(self):
        self.players = []

    def find_player(self, number):
        for player in self.players:
            if player.get_number() == number:
                return player
        return None

    def add_player(self, name=None, credit=None, number=None, age=None):
        if not name:
            name = input("Enter player name: ")
        if not credit:
            credit = int(input("Enter player credit: "))
        if not number:
            number = int(input("Enter player number: "))
        if not age:
            age = int(input("Enter player age: "))
            
        player = Player(name, credit, number, age)
        self.players.append(player)
        #print(f"Player {player.get_name()} (No. {player.get_number()}) added successfully.")



    def update_player(self):
        number = int(input("Enter player number to update: "))
        player = self.find_player(number)
        if player:
            name = input("Enter new player name (leave blank to keep current name): ")
            credit = int(input("Enter new player credit (leave blank to keep current credit): ") or player.get_credit())
            age = int(input("Enter new player age (leave blank to keep current age): ") or player.get_age())
            player.set_name(name) if name else None
            player.set_credit(credit)
            player.set_age(age)
            print(f"Player {player.get_name()} (No. {player.get_number()}) updated successfully.")
        else:
            print(f"No player with number {number} found.")

    def delete_player(self):
        number = int(input("Enter player number to delete: "))
        player = self.find_player(number)
        if player:
            self.players.remove(player)
            print(f"Player {player.get_name()} (No. {player.get_number()}) deleted successfully.")
        else:
            print(f"No player with number {number} found.")

    def display_players(self):  
        Utils.playerHeader()   
        for player in self.players:
            
            # print(f"Player Name: {player.get_name()}, Number: {player.get_number()}, Age: {player.get_age()}, Level: {player.get_level()}")
            print(Utils.PlayerFormat(player.get_name(), player.get_credit(), player.get_level(), player.get_number(), player.get_age()))
        Utils.playerTableEnd()

    def display_players_by_level(self, level):
        for player in self.players:
            if player.get_level() == level:
                print(f"Player Name: {player.get_name()}, Number: {player.get_number()}, Age: {player.get_age()}")

