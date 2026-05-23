#rock paper scissor game
import random
l = ["rock", "paper", "scissor"]
while True:
    print("Press 1 to Play AND Press 2 to Exit.")
    ch = int(input("Enter choice:"))
    
    if (ch==1):
        user_point = 0
        comp_point = 0  #variable define
        for i in range(1,7):

            user_input = input("Enter rock, paper or scissor: ")
            if user_input not in l:
                print("Invalid input. Please try again.")
                continue
            computer_input = random.choice(l)
            print(f"Computer chose: {computer_input}")
            if user_input == computer_input:
                print("It's a tie!")
            elif (user_input == "rock" and computer_input == "scissor") or (user_input == "paper" and computer_input == "rock") or (user_input == "scissor" and computer_input == "paper"):
                print("You win!")
                user_point += 1
            else:
                print("you lose.")
                comp_point += 1
        print("<GAME OVER>")
        if(user_point > comp_point):
            print("Congratulations! You won this round.")
        elif(user_point == comp_point):
            print("This round is tie! Well played.")
        else:
            #print("You lose this round, Better luck next time.")
            print("ae lelelele meoww gop gop gop gop")

    elif(ch==2):
        print("closing the game...")

    else:
        print("Invalid choice. Try again..")
