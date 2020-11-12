the_board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '}


def show_board():
    print(the_board['1'] + '|' + the_board['2'] + '|' + the_board['3'])
    print('-+-+-')
    print(the_board['4'] + '|' + the_board['5'] + '|' + the_board['6'])
    print('-+-+-')
    print(the_board['7'] + '|' + the_board['8'] + '|' + the_board['9'])


def game():
    turn = 'X'
    count = 0
    while True:
        print("\n")
        show_board()
        print("\n")

        print("' " + turn + " ' turn,\nwhich place you choose? ")
        choose = input()

        if the_board[choose] == " ":
            the_board[choose] = turn
        else:
            print("this place was chosen, please try another place to choose.")
            while True:
                choose = input()
                if the_board[choose] != " ":
                    print("this place was chosen, please try another place to choose.")
                else:
                    the_board[choose] = turn
                    break
            continue

        count += 1

        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':
                show_board()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                restart_game()
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ': 
                show_board()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                restart_game()
                break
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':
                show_board()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                restart_game()
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':
                show_board()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                restart_game()
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
                show_board()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                restart_game()
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
                show_board()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                restart_game()
                break
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ': 
                show_board()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                restart_game()
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
                show_board()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                restart_game()
                break

        if count == 9:
            print('\n')
            print('it\'s a tie!')
            restart_game()
            turn = 'O'
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


def restart_game():
    print('want to play again? y/n')
    restart = input()
    if restart == 'y' or restart == 'Y':
        count = 0
        for v in the_board:
            the_board[v] = ' '
        game()
    else:
        print('Good Bye :)')


game()
