import random
player_score = 0
computer_score = 0
player_rock_count = 0
player_scissor_count = 0
player_paper_count = 0
while True:
    player_input = input("make a move (r/s/p)")
    if player_input == 'sc':
        print('human: '+str(player_score)+', computer: ' + str(computer_score))
        continue
    comp_move = random.randint(0, 2)
    if player_rock_count > player_scissor_count and player_rock_count > player_paper_count:
        comp_move = 2
    elif player_scissor_count > player_rock_count and player_scissor_count > player_paper_count:
        comp_move = 0
    elif player_paper_count > player_rock_count and player_paper_count > player_scissor_count:
        comp_text = 1
    comp_output = None
    comp_text = None
    if comp_move == 0:
        comp_output = 'r'
        comp_text = 'rock'
    elif comp_move == 1:
        comp_output = 's'
        comp_text = 'scissors'
    elif comp_move == 2:
        comp_output = 'p'
        comp_text = 'paper'

    player_text = None
    if player_input == 'r':
        player_text = 'rock'
        player_rock_count = player_rock_count + 1
    elif player_input == 's':
        player_text = 'scissors'
        player_scissor_count = player_scissor_count + 1
    elif player_input == 'p':
        player_text = 'paper'
        player_paper_count = player_paper_count + 1

    if player_input == comp_output:
        continue
    outcome = None
    if (player_input == 'r' and comp_output == 's') or \
        (player_input == 's' and comp_output == 'p') or \
            (player_input == 'p' and comp_output == 'r'):
        outcome = 'Win'
        player_score = player_score + 1
    else:
        outcome = 'Lose'
        computer_score = computer_score + 1

    print('You chose ' +player_text+' and the computer chose '+comp_text+'. You ' +outcome+ '!')
    play_again_input = input("Do you want to play again? (Y/N)")
    if play_again_input == 'y':
        continue
    elif play_again_input == 'n':
        print("Thanks bye!")
        break
