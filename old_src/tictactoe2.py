# 2 - Basic logic changed; Bugs removed; global variables altered
OUTCOME = 'DRAW'
USE_CLEAN_BOARD = True
# USE_CLEAN_BOARD = False


def check_input(input, ARR):
    '''
    The fuctions return True if the input is valid.
    '''
    return input in [str(x) for x in ARR if x != 'X' and x != 'O'] and input != ''


def process_input(input, player, ARR):
    '''
    The module alters the values of the global variable ARR.
    '''
    ARR[int(input)-1] = player


def process_input_dict(dict):
    pass


def get_board(ARR):
    global USE_CLEAN_BOARD
    '''
    The function returns the current state of the game board.
    '''
    def make_board(x):
        return f'''{x[0]} | {x[1]} | {x[2]}
---------
{x[3]} | {x[4]} | {x[5]}
---------
{x[6]} | {x[7]} | {x[8]}'''
    return make_board([' ' if not isinstance(x, str) else x for x in ARR] if USE_CLEAN_BOARD else ARR)  # the list comprehension just removes the integers from the list and replace them with ' '


def alternate_players(player):
    '''
    The function alternates between the two players.
    '''
    if player == 'X':
        return 'O'
    else:
        return 'X'


def game_ended(ARR):
    global OUTCOME
    '''
    This function returns True if the game has ended and sets the value of the global variable OUTCOME.
    '''
    possibilities = {
        'col1': (ARR[0], ARR[1], ARR[2]),
        'col2': (ARR[3], ARR[4], ARR[5]),
        'col3': (ARR[6], ARR[7], ARR[8]),
        'row1': (ARR[0], ARR[3], ARR[6]),
        'row2': (ARR[1], ARR[4], ARR[7]),
        'row3': (ARR[2], ARR[5], ARR[8]),
        'diag1': (ARR[0], ARR[4], ARR[8]),
        'diag2': (ARR[2], ARR[4], ARR[6]),
    }

    X_won = ('X', 'X', 'X') in possibilities.values()
    O_won = ('O', 'O', 'O') in possibilities.values()

    if X_won:
        OUTCOME = 'X WON THE GAME'
    elif O_won:
        OUTCOME = 'O WON THE GAME'

    return X_won or O_won or [] == list(
        filter(lambda x: not isinstance(x, str), ARR))


def main():
    replay = True
    while replay:
        ARR = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        player = 'X'
        print('WELCOME TO TICTACTOE')
        print('X will go first')
        print('In order to change the board display mode (clean/numbered) uncomment line 4 of the game code')
        while not game_ended(ARR):
            print()
            print(get_board(ARR))
            print()
            val = input(f'{player}==> Input location (1-9): ')
            if check_input(val, ARR):
                process_input(val, player, ARR)
                player = alternate_players(player)

        print('='*60)
        print(get_board(ARR))
        print()
        print('THE GAME ENDED')
        print(OUTCOME)
        print('='*60)

        re = input('Do you want to replay? y/n: ')
        if re.lower() == 'y' or re.lower() == 'yes':
            pass
        else:
            break


if __name__ == "__main__":
    main()
