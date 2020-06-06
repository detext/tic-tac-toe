# 1.1 - Clean mode added; X will go first added; Bugs removed

ARR = [1, 2, 3, 4, 5, 6, 7, 8, 9]
USE_CLEAN_BOARD = True
# USE_CLEAN_BOARD = False
OUTCOME = 'DRAW'


def check_input(input):
    global ARR
    '''
    The fuctions return True if the input is valid
    '''
    return input in [str(x) for x in ARR if x != 'X' and x != 'O'] and input != ''


def process_input(input, player):
    global ARR
    '''
    The module alters the values of the global variable ARR
    '''
    ARR[int(input)-1] = player


def process_input_dict(dict):
    pass


def get_board():
    # global ARR
    '''
    The function returns the current state of the game board
    '''
    def make_board(x):
        return f'''{x[0]} | {x[1]} | {x[2]}
---------
{x[3]} | {x[4]} | {x[5]}
---------
{x[6]} | {x[7]} | {x[8]}'''
    return make_board([' ' if isinstance(x, int) else x for x in ARR] if USE_CLEAN_BOARD else ARR)  # the list comprehension just removes the integers from the list and replace them with ' '


def alternate_players(player):
    '''
    The function alternates between the two players
    '''
    if player == 'X':
        return 'O'
    else:
        return 'X'


def game_ended():
    global ARR, OUTCOME
    '''
    This function returns True if the game has ended
    '''
    # 10.5 = X and -5.5 = O
    # Dont change these values
    converted_arr = [10.5 if x == 'X' else -
                     5.5 if x == 'O' else x for x in ARR]
    possibilities = {
        'col1': sum((converted_arr[0], converted_arr[1], converted_arr[2])),
        'col2': sum((converted_arr[3], converted_arr[4], converted_arr[5])),
        'col3': sum((converted_arr[6], converted_arr[7], converted_arr[8])),
        'row1': sum((converted_arr[0], converted_arr[3], converted_arr[6])),
        'row2': sum((converted_arr[1], converted_arr[4], converted_arr[7])),
        'row3': sum((converted_arr[2], converted_arr[5], converted_arr[8])),
        'diag1': sum((converted_arr[0], converted_arr[4], converted_arr[8])),
        'diag2': sum((converted_arr[2], converted_arr[4], converted_arr[6])),
    }
    X_won = 31.5 in possibilities.values()
    O_won = -16.5 in possibilities.values()
    state = X_won or O_won or [] == list(
        filter(lambda x: not isinstance(x, str), ARR))
    if X_won:
        OUTCOME = 'X WON THE GAME'
    elif O_won:
        OUTCOME = 'O WON THE GAME'
    return state


def main():
    global ARR, OUTCOME
    replay = True
    while replay:
        print('WELCOME TO TICTACTOE')
        print('X will go first')
        print('In order to change the board display mode (clean/numbered) uncomment line 4 of the game code')
        player = 'X'
        while not game_ended():
            print()
            print(get_board())
            print()
            val = input(f'{player}==> Input location (0-9): ')
            if check_input(val):
                process_input(val, player)
                player = alternate_players(player)

        print('='*60)
        print(get_board())
        print()
        print('THE GAME ENDED')
        print(OUTCOME)
        print('='*60)

        re = input('Do you want to replay? y/n: ')
        if re.lower() == 'y' or re.lower() == 'yes':
            ARR = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            OUTCOME = 'DRAW'
        else:
            break


if __name__ == "__main__":
    main()
