def rps():
 while True:
    choice = input("Do wanna play a game of Rock-paper-scissor? yes/no\n")
    if choice == 'yes':
        player1=input("Player 1, Enter Your Choice:")
        player2 = input("Player 2, Enter Your Choice:")
        if player1 == player2:
            print("Its a tie")

        elif player1 == 'rock':
            if player2 == 'scissors':
                print("Player 1 wins\n Congratulations")
            else:
                print("Player 2 wins\n Congratulations")
        elif player1 == 'scissors':
            if player2 == 'paper':
                print("Player1 wins\n Congratulations")
            else:
                print("Player 2 wins\n Congratulations")
        elif player1 == 'paper':
            if player2 == 'rock':
                print("Player1 wins\n Congratulations")
            else:
                print("Player2 wins\n Congratulations")
    else:
        print("Run again to play!!")
        break
rps();

