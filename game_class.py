import random

class Player:

    player_count = 0
    player_list = []
    target_score = 5

    def __init__(self, player_name = "scrub", player_type = None, player_level = 0, player_record = None):
        self.name = player_name
        self.type = player_type
        self.dribbles = 0
        self.player_record = []
        self.position = 0

        self.on_offense = True
        if (self.type == "Lebron"):
            self.offense = 80
            self.defense = 80       
        elif (self.type == "Steph"):
            self.offense = 90
            self.defense = 70
        elif (self.type == "Giannis"):
            self.offense = 70
            self.defense = 90
        elif (self.type == "Jordan"):
            self.offense = 90
            self.defense = 90
        elif (self.type == "Monstar"):
            self.offense = 80
            self.defense = 100        
        else:
            self.offense = 65
            self.defense = 65

        Player.player_count += 1
        Player.player_list.append(self)

        print("Welcome to King of the Court " + self.name + "!")
        print("You have an offensive rating of " + str(self.offense) + " and a defensive rating of " + str(self.defense) + ".")

        
        if(Player.player_count == 1):
            print("There is " + str(Player.player_count) + " player on the court: ")
            print(Player.player_list[0].name)
        else:
            print("There are " + str(Player.player_count) + " players on the court: ")
            for player in range(len(Player.player_list)):
                print(Player.player_list[player].name)

    # method for monitoring position on court
    def player_position(self):
        user_choice = input(self.name + ", press L and enter to go left, R and enter to go right, or anything else to stay where you are. \n")
        if(user_choice.upper() == "L"):
            self.position -= 1
            self.dribbles += 1
        elif(user_choice.upper() == "R"):
            self.position += 1
            self.dribbles += 1
        else:
            self.position == 1 
        return self.position    


    # method for monitoring number of dribbles (limit of 2)

    # method for monitoring if player has reached target score
    def check_win(self):
        num_wins = sum(self.player_record)
        if (num_wins == Player.target_score):
            print(self.name + " is the King of the Court!")
            return True
        else:
            return False

    # method for determining probability of scoring a point depending on defensive rating and position
    def shot_probability(self, opponent_defense, opponent_position):
        if (self.position == opponent_position):
            return  self.offense - 0.5 * opponent_defense
        elif (abs(self.position - opponent_position) == 1):
            return self.offense - .25 * opponent_defense
        else:
            return self.offense


# class for determining results of each matchup
class Round:

    def __init__(self, player1, player2):
        self.offensive_player = player1
        self.defensive_player = player2
    
    def matchup_result(self):
        shot_prob = self.offensive_player.shot_probability(self.defensive_player.defense, self.defensive_player.position)
        if float(random.randint(0, 100) < shot_prob):
            print("You made it")
            self.offensive_player.player_record.append(1)
            #leaves offensive player at front of list and pops off defensive player and places player to end of list
            # print(Player.player_list)
            temp = Player.player_list.pop(1)
            Player.player_list.append(temp)
            for player in range(len(Player.player_list)):
                print(Player.player_list[player].name + ": " + str(sum(Player.player_list[player].player_record))) 

        else:
            print("You missed it. Get to the back of the line.")
            self.offensive_player.player_record.append(0)
            #pops off offensive player and moves player to end of list
            # print(Player.player_list)
            temp = Player.player_list.pop(0)
            Player.player_list.append(temp)            
            print("This is the current lineup: ")
            for player in range(len(Player.player_list)):
                print(Player.player_list[player].name + ": " + str(sum(Player.player_list[player].player_record))) 

    def turnover(self):
        print("You turned it over. Get to the back of the line.")
        self.offensive_player.player_record.append(0)
        #pops off offensive player and moves player to end of list
        # print(Player.player_list)
        temp = Player.player_list.pop(0)
        Player.player_list.append(temp)            
        for player in range(len(Player.player_list)):
            print(Player.player_list[player].name + ": " + str(sum(Player.player_list[player].player_record))) 




