class Utils:
    def PlayerFormat(name,credit,level,No,age):
        return "| %-*s | %-*s | %-*s | %-*s | %-*s |" % (20, name, 14, "{:.2f}".format(credit), 12, level, 5, No,5,age)
    def teamsFormat(name,numofplayer,avgcredit,avgage):
        return "| %-*s | %-*s | %-*s | %-*s |" %(20,name,19,numofplayer,21,"{:.2f}".format(avgcredit),12,"{:.2f}".format(avgage))

    def DisplayPlayerFromAllTeamsFormat(name,credit,level,No,age,team):
        return "| %-*s | %-*s | %-*s | %-*s | %-*s | %-*s |" % (20,name,14,"{:.2f}".format(credit),12,level,5,No,5,age,9,team)
    def GamesFormat(first,option,second):
        return     "| %-*s | %-*s | %-*s |" %(17,first,4,option,17,second)
   
    def RecordFormat(round,game,win,lose):
        return "| %-*s | %-*s | %-*s | %-*s |" %(5,round,4,game,12,win,12,lose)



    @staticmethod
    def RecordHeader():
            print("+-------+------+--------------+--------------+")
            print("| Round | Game | Winning Team | Losing team  |")
            print("+-------+------+--------------+--------------+")

    @staticmethod
    def RecordEnd():
            print("+-------+------+--------------+--------------+")

    @staticmethod
    def GameHeader():
            print("+-------------------+------+-------------------+")
            print("| First Team        |      | Second Team       |")
            print("+-------------------+------+-------------------+")

    @staticmethod
    def GameEnd():
            print("+-------------------+------+-------------------+")

    @staticmethod
    def teamsHeader():
            print("+----------------------+---------------------+-----------------------+--------------+")
            print("| Team Name            | Number of Players   | Average Player Credit | Average Age  |")
            print("+----------------------+---------------------+-----------------------+--------------+")

    @staticmethod
    def teamTableEnd():
            print("+----------------------+---------------------+-----------------------+--------------+")

    @staticmethod
    def playerHeader():
            print("+----------------------+----------------+--------------+-------+-------+")
            print("| Player Name          | Credit         | Level        | No    | Age   |")
            print("+----------------------+----------------+--------------+-------+-------+")

    @staticmethod
    def playerTableEnd():
            print("+----------------------+----------------+--------------+-------+-------+")

    @staticmethod
    def DisplayPlayerFromAllTeamsHeader():
            print("+----------------------+----------------+--------------+-------+-------+-----------+")
            print("| Player Name          | Credit         | Level        | Age   | No    | Team      |")
            print("+----------------------+----------------+--------------+-------+-------+-----------+")

    @staticmethod
    def DisplayPlayerFromAllTeamsEnd():
            print("+----------------------+----------------+--------------+-------+-------+-----------+")
