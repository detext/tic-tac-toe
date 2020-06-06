# 3 - Basic logic changed; main() changed; get_boad() changed
USE_CLEAN_BOARD = False
#USE_CLEAN_BOARD = True


def check_input(input, ARR):
    '''
    The fuctions return True if the input is valid.
    '''
    return input in [str(x) for x in ARR if x not in ('X', 'O')] and input != ''


def process_input(input, player, ARR):
    '''
    The module alters the values of the variable ARR.
    '''
    ARR[int(input)-1] = player


def get_board(ARR, styling='default'):
    '''
    The function returns the current state of the game board.

    styling option : default/numbered/clean
    '''
    if styling == 'default':
        clean_board = USE_CLEAN_BOARD
    elif styling == 'numbered':
        clean_board = False
    elif styling == 'clean':
        clean_board = True

    def make_board(x):
        return f'''{x[0]} | {x[1]} | {x[2]}
---------
{x[3]} | {x[4]} | {x[5]}
---------
{x[6]} | {x[7]} | {x[8]}'''
    return make_board([' ' if isinstance(x, int) else x for x in ARR] if clean_board else ARR)  # the list comprehension just removes the integers from the list and replace them with ' '


def alternate_players(player):
    '''
    The function alternates between the two players.
    '''
    if player == 'X':
        return 'O'
    return 'X'


def get_winner(ARR, player):
    '''
    The function returns the outcome of the game and the winnning move.
    '''
    win_possibilities = {
        'col1': (0, 1, 2),
        'col2': (3, 4, 5),
        'col3': (6, 7, 8),
        'row1': (0, 3, 6),
        'row2': (1, 4, 7),
        'row3': (2, 5, 8),
        'diag1': (0, 4, 8),
        'diag2': (2, 4, 6),
    }
    for a, b, c in win_possibilities.values():
        if {player} == {ARR[a], ARR[b], ARR[c]}:
            return (player, (a, b, c))
    else:
        return ('', ())


def main():
    print('WELCOME TO TICTACTOE')
    print('X will go first')
    print('In order to change the board display mode (clean/numbered) uncomment line 3 of the game code')
    replay = True
    while replay:
        ARR = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        PLAYER = 'X'
        for _ in range(9):
            print('\n' + get_board(ARR) + '\n')
            while True:
                val = input(f'{PLAYER}==> Input location (1-9): ')
                if check_input(val, ARR):
                    break
                else:
                    print('\n'+'Invalid Input!'+'\n')
            process_input(val, PLAYER, ARR)
            outcome, winning_move = get_winner(ARR, PLAYER)
            if outcome:
                break
            PLAYER = alternate_players(PLAYER)
        else:
            outcome = 'DRAW'

        print('='*60)
        if outcome == 'DRAW':
            print('\n' + get_board(ARR) + '\n')
        else:
            print('\n' + get_board(
                [outcome if x in winning_move else x for x in range(9)], 'clean') + '\n')
        if outcome == 'DRAW':
            print('GAME ENDED IN A DRAW')
        else:
            print(f'{outcome} WON THE GAME')
        print('='*60)

        re = input('Do you want to replay? y/n: ')
        if re.lower() == 'y' or re.lower() == 'yes':
            pass
        else:
            break


if __name__ == "__main__":
    main()
