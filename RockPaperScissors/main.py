import random

#declare variables for available choices and their values
choices = ['R','P','S']
choices_dict = {'R':'Rock','P':'Paper','S':'Scissors'}

print('Welcome To Rock Paper Scissors! \nYou can pick between R for Rock, P for Paper and S for Scissors')

while choices:
    #cpu's choice
    cpu = random.choice(choices)
    #user's choice
    user = input('\nYour Pick? \n')
    user = str(user).upper()
    #compare and provide result
    if user in choices:
        print('Player(' + choices_dict[user] + '):CPU(' + choices_dict[cpu] + ')')
        if user == cpu: print('Tied. Try again')
        
        elif user == 'R':
            if cpu == 'S': print('You won! Thanks for playing'); break
            elif cpu == 'P': print('You lost! Try again')
                
        elif user == 'P':
            if cpu == 'R': print('You won! Thanks for playing'); break
            elif cpu == 'S': print('You lost! Try again')
                
        elif user == 'S':
            if cpu == 'P': print('You won! Thanks for playing'); break
            elif cpu == 'R': print('You lost! Try again')

    #retry if input is wrong
    else:
        print('Oops! Wrong Input. Try again')


