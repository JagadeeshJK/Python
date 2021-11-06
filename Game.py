user1_answer = input("%s, do yo want to choose rock, paper or scissors?")
user2_answer = input("%s, do yo want to choose rock, paper or scissors?")
def compare(u1,u2):
      if u1 == u2:
           return("it's a tie")
      elif u1 == 'rock':
        if u2 == 'scissors':
           return("Rock wins")
        else:
           return("paper wins")
      elif u1 == 'scissors':
        if u2 == 'paper':
           return("scissors win")
        else:
           return("rocket wins")
      elif u1 == 'paper':
        if u2 == 'rock':
            return("paper wins")
        else:
            return("scissors win")
      else:
            return("invalid input you have not entered rock, paper or scissors, try again.")
            sys.exit()
print(compare(user1_answer, user2_answer))
