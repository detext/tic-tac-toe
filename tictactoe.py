import argparse

parser = argparse.ArgumentParser(description='A TICTACTOE GAME')
parser.add_argument('-n', '--numbered', action='store_true',
                    help='displays the board with boxes numbered')
NUMBERED = parser.parse_args().numbered


def reset_game():
    '''
    the function resets the game.
    '''
    global ARR, PLAYER, OUTCOME
    # for ARR i have used numbers instead of indexes
    # as it was easier to implement input with numbers
    # from 1 to 9 instead of using indexes which start from 0.
    # To turn the input number to an index, just subtract 1 
    # from the input value as done in the process input function.
    ARR = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    PLAYER = 'X'
    OUTCOME = {'player_won': None, 'winning_move': None}


def check_input(point):
    '''
    The functions return True if the input is valid.
    '''
    return point in (str(x) for x in ARR if x not in ('X', 'O'))


def process_input(point):
    '''
    The function alters the values of the variable ARR.
    '''
    global ARR
    ARR[int(point)-1] = PLAYER


def get_board(ARR, numbered=NUMBERED):
    '''
    The function returns the current state of the game board.

    styling options : default|numbered|clean
    '''

    def make_board(x):
        return f'''{x[0]} | {x[1]} | {x[2]}
--+---+--
{x[3]} | {x[4]} | {x[5]}
--+---+--
{x[6]} | {x[7]} | {x[8]}'''
    # the list comprehension below removes the integers from the list
    # and replace them with ' '(space) if numbered_board is not true
    return make_board([' ' if isinstance(x, int) else x for x in ARR] if not numbered else ARR)


def alternate_players():
    '''
    The function alternates between the two players.
    '''
    global PLAYER
    if PLAYER == 'X':
        return 'O'
    return 'X'


def get_game_outcome():
    '''
    The function returns the outcome of the game and the winning move.
    '''
    # these values are indexes
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
        if {PLAYER} == {ARR[a], ARR[b], ARR[c]}:
            OUTCOME['player_won'] = PLAYER
            OUTCOME['winning_move'] = (a, b, c)


def main():
    '''
    The main tictactoe game.
    '''
    global ARR, PLAYER, OUTCOME
    print('\nWELCOME TO TICTACTOE')
    print('X will go first')
    print('Run with optional argument -n for numbered board')
    replay = True

    while replay:

        reset_game()

        for _ in range(9):

            print('\n' + get_board(ARR) + '\n')

            while True:
                point = input(f'{PLAYER} ==> Input location (1-9): ')
                if check_input(point):
                    process_input(point)
                    break
                print('\n'+'Invalid Input!'+'\n')

            get_game_outcome()

            if OUTCOME['player_won']:
                print('\n' + get_board([OUTCOME.get("player_won") if x in OUTCOME.get(
                    "winning_move") else (x+1) for x in range(9)], numbered=False) + '\n')
                print(f'{OUTCOME.get("player_won")} WON THE GAME')
                print('='*60)
                break

            PLAYER = alternate_players()

        else:
            print('='*60)
            print('\n' + get_board(ARR) + '\n')
            print('GAME ENDED IN A DRAW')
            print('='*60)

        re = input('Do you want to replay? y/n: ')
        if re.lower() in ('y', 'yes'):
            pass
        else:
            break


if __name__ == "__main__":
    main()
