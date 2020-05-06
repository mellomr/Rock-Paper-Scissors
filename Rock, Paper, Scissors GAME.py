import random
def game():
    life=input('How many goes do you want?')
    score=0
    CPUscore=0
    while life == '':
        life=input('How many goes do you want?')
       
        
    for life in range(int(life)):
        choice=input('Choose your attack: (R)ock, (P)aper, (S)cissors')
        choice=choice.capitalize()
        CPUchoice=['R', 'P', 'S']
        CPUchoice=random.choice(CPUchoice)
        print('CPU:',CPUchoice)

        
        if choice == CPUchoice:
            print('Draw!')

        elif choice == 'R':
            if CPUchoice == 'P':
                print('You Lose!', 'CPU Wins')
                CPUscore=CPUscore+1
            else:
                print('You Win!','CPU Loses')
                score=score+1

        elif choice == 'P':
            if CPUchoice == 'S':
                print('You Lose!', 'CPU Wins')
                CPUscore=CPUscore+1

            else:
                print('You Win!', 'CPU Loses')
                score=score+1

        elif choice == 'S':
            if CPUchoice == 'R':
                print('You Lose!', 'CPU Wins')
                CPUscore=CPUscore+1
            else:
                print('You Win!', 'CPU Loses')
                score=score+1
        else:
            print('Invalid')

            

    print('------------------------------------------------')


    print('You have had', life+1, 'goes')
    print('Your score is', score)
    print('CPU score is', CPUscore)

    if score == CPUscore:
        print('It is a DRAW!')

    elif score > CPUscore:
        print('You WON! You beat the CPU')

    else:
        print('Unlucky, the CPU won')
        
    print('------------------------------------------')    
    replay=input('Do you want to play again?')

    if replay == 'yes' or replay == 'Yes':
        game()

    else:
        print('Game Over')


    return

game()
