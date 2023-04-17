class Player:
    def __init__(self, name, credit, number, age):
        self.name = name
        self.credit = credit
        self.number = number
        self.age = age
        #self.team = team

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_credit(self):
        return self.credit

    def set_credit(self, credit):
        self.credit = credit

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    # def get_team(self):
    #     return self.team

    # def set_team(self, team):
    #     self.team = team

    def get_level(self):
        if self.credit < 1000:
            return "Edge"
        elif 1000 <= self.credit < 1500:
            return "Common"
        elif 1500 <= self.credit < 2000:
            return "Core"
        else:
            return "Expert"
