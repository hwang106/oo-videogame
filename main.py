import game_class

player1 = game_class.Player("Bugs", "Steph")
player2 = game_class.Player("Fudd", "Giannis")
player3 = game_class.Player("Rando")

# Since there are always only two players competing at a time in King of the Court, the code implemented below accesses those players via the first two indices of a list of all Player objects instantiated, instead of the variable name of the instance.
# Outer while loop runs the game until target number of matchups are won (default is 5)
while(not game_class.Player.player_list[0].check_win()):
    print(game_class.Player.player_list[0].name + ", you are up on offense.")
    print(game_class.Player.player_list[1].name + ", you are up for defense.")
    # Inner while loop runs the matchup until a shot is taken or a turnover occurs without shooting after 2 dribble limit
    game_class.Player.player_list[0].dribbles = 0
    game_class.Player.player_list[1].dribbles = 0
    was_shot = False
    while(game_class.Player.player_list[0].dribbles < 2 and not was_shot):
        game_class.Player.player_list[0].player_position()
        game_class.Player.player_list[1].player_position()
        is_shooting = input(game_class.Player.player_list[0].name + ", do you want to shoot it? Y/N \n")
        if(is_shooting.upper() == "Y"):
            was_shot = True
            round = game_class.Round(game_class.Player.player_list[0], game_class.Player.player_list[1])
            round.matchup_result()
        elif(game_class.Player.player_list[1].dribbles >= 2):
            was_shot = False
            round = game_class.Round(game_class.Player.player_list[0], game_class.Player.player_list[1]) 
            round.turnover()

        

