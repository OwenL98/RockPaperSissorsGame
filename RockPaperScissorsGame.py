from random import choice

actions_list = ('rock', 'paper','sissors')
rules = 'This is rock, paper, sissors.\nRules:\nRock beats sissors\nPaper beats rock\nSissors beats paper\nOne point per win\nThe game will not start until you enter rock, paper or sissors (no spaces after)\nIf you want to end the game at any point enter \'end game\'\n'
print (rules)
user_word = input ('Please enter either rock, paper or sissors\n')



def end_game(user_word):

    if user_word == 'end game':
        print ('The game has now ended')

end_game(user_word)

def result (end_game):

    computer_output = choice(actions_list)
    user_score = 0
    computer_score = 0

    print('computer:',computer_output)
    if user_word == computer_output:
        print ('draw')
        print('you ' + str(user_score), 'computer ' + str(computer_score))
    elif user_word == 'rock' and computer_output == 'sissors' or user_word == 'paper' and computer_output == 'rock' or user_word == 'sissors' and computer_output == 'paper':
        print ('user wins')
        user_score = user_score + 1
        print('you ' + str(user_score), 'computer ' + str(computer_score))
    elif user_word == 'rock' and computer_output == 'paper' or user_word == 'sissors' and computer_output == 'rock' or user_word == 'paper' and computer_output == 'sissors':
        print('computer wins')
        computer_score = computer_score + 1
        print('you ' + str(user_score), 'computer ' + str(computer_score))


#two values creates a tuple but one result does not
    return user_score, computer_score




while user_word not in actions_list:
    if user_word == 'end game':
        break
    user_word = input ('enter either rock, paper or sissors\n')
    end_game(user_word)
else:
    result(end_game)



