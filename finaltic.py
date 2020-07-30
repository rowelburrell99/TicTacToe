# Defines the board as a grid system with 10 empty values.
# By inputting an empty string into the first value, users can only input a value of 1-9 instead of 0-9.
board = [' ' for x in range(10)]

# Clears the board
def clear():
    board.clear()

# Reallocates the empty values to the board
def reset():
    global board
    board = [' ' for x in range(10)]
    return board


def LetterPosition(letter, pos):
    board[pos] = letter


# User inputs their name, this string is returned into the global variable so that it can be accessed throughout the program.
def player():
    global player1name
    player1name = input("\nEnter name for player 1: ")
    return player1name


def player2():
    global player2name
    player2name = input("Enter name for player 2: ")
    return player2name


# Searches for an empty position in the board, returns true there is a position free (i.e. doesnt have an 'X' or 'O' in.)
def emptyspace(pos):
    return board[pos] == ' '


def Example():
    print('\nExample of a diagonal win: \t\t\t\tExample of a horizontal win: \t\t\t\tExample of a vertical win:')
    print('    |    | '   '   \t\t\t\t\t\t\t\t\t |    |' '   \t\t\t\t\t\t\t\t\t |    |')
    print(' X'  '  |   '' |  ' '\t\t\t\t\t\t\t\t  X'  '  | X '' | X ' '\t\t\t\t\t\t\t\t  X'  '  |  ''  |   ')
    print('    |    |' '   \t\t\t\t\t\t\t\t\t |    |' '   \t\t\t\t\t\t\t\t\t |    |')
    print('--------------' '\t\t\t\t\t\t\t\t --------------' '\t\t\t\t\t\t\t\t --------------')
    print('    |    |'    '   \t\t\t\t\t\t\t\t\t |    |' '   \t\t\t\t\t\t\t\t\t |    |')
    print(' '  '   | X ' ' |  ' '   \t\t\t\t\t\t\t\t\t |    |' '\t\t\t\t\t\t\t\t      X'  '  |  ''  |   ')
    print('    |    |' '   \t\t\t\t\t\t\t\t\t |    |' '   \t\t\t\t\t\t\t\t\t |    |')
    print('--------------' '\t\t\t\t\t\t\t\t --------------' '\t\t\t\t\t\t\t\t --------------')
    print('    |    |' '   \t\t\t\t\t\t\t\t\t |    |' '   \t\t\t\t\t\t\t\t\t |    |')
    print('  ' '  |   ' ' | X ' '\t\t\t\t\t\t\t\t\t |    |' '\t\t\t\t\t\t\t\t      X'  '  |  ''  |   ')
    print('    |    |' '   \t\t\t\t\t\t\t\t\t |    |' '   \t\t\t\t\t\t\t\t\t |    |')


def boardInstructions():
    print('\nTic Tac Toe is a game in which the person who get a row of three (diagonally, horizontally, vertically) with their given symbol (X or O) wins. ')
    print('Below is a grid layout, this allows you to  see the where your letter will be placed based on your input value of 1-9.')
    print('    |    |')
    print(' 1'  '  | 2 '' | 3 ')
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' 4'  '  | 5 ' ' | 6')
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' 7' '  | 8 ' ' | 9 ')
    print('    |    |')


# Layout of the board, board[x] being the position of the space.
def printBoard(board):
    print('    |    |')
    print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
    print('    |    |')


# If the positions on the board are taken with the same letter, then the user has won.
def WinCondition(board, letter):
    return (board[7] == letter and board[8] == letter and board[9] == letter) \
           or (board[4] == letter and board[5] == letter and board[6] == letter) \
           or (board[1] == letter and board[2] == letter and board[3] == letter) \
           or (board[1] == letter and board[4] == letter and board[7] == letter) \
           or (board[2] == letter and board[5] == letter and board[8] == letter) \
           or (board[3] == letter and board[6] == letter and board[9] == letter) \
           or (board[1] == letter and board[5] == letter and board[9] == letter) \
           or (board[3] == letter and board[5] == letter and board[7] == letter)


# Prompts the user to input a value, i.e. selecting a position. If the space isn't occupied, the letter is input into the board position.
def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if emptyspace(move):
                    run = False
                    LetterPosition('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def playerMove2():
    run = True
    while run:
        move = input('Please select a position to place an \'O\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if emptyspace(move):
                    run = False
                    LetterPosition('O', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


""" 
1. Locates the best possible move for the AI to make.
2. if an empty slot is available, it's a possible move.
3. If there are any possible moves that the player can make that will win the game, block it.
4. Identify a corner position (1, 3, 7, 9)
5. If there is more than one corner to select from, choose at random.
6. Try to secure position 5 (the center square).
7. Identifies an edge position (2, 4, 6, 8)
8. If there is more than one edge to select from, choose at random.
"""
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if WinCondition(boardCopy, let):
                move = i
                return move

    chooseCorner = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            chooseCorner.append(i)

    if len(chooseCorner) > 0:
        move = selectRandom(chooseCorner)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    chooseEdge = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            chooseEdge.append(i)

    if len(chooseEdge) > 0:
        move = selectRandom(chooseEdge)

    return move


# Select randomly from the range of 0 to the length of the list, i.e. however many options are left.
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


# Checks to see if the board has any empty empty values.
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


"""
1. Gets the users names (they input them at the start).
2. Prints the board
3. Runs a while loop so long that x < 9, every time a player makes a move, the variable x is incremented by 1.
4. After every move the 'WinCondition' function is executed to see if a player has won.
5. If a player has won, they will be awarded 1 point and the loop is broken.
6. When the game ends, they will also be prompted to play another game.
"""
def pvp():
    player2()
    print('\nWelcome to Tic Tac Toe!')
    printBoard(board)
    p1score = 0
    p2score = 0
    a = 0
    while a < 1:
        x = 0
        while x < 9:
            isBoardFull(board)
            playerMove()
            printBoard(board)
            x = x + 1
            if WinCondition(board, 'X'):
                print(player1name + ' won this round! Good Job!')
                p1score += 1
                break
            if x == 9:
                print("The game is tied!")
                break
            playerMove2()
            printBoard(board)
            x = x + 1
            if WinCondition(board, 'O'):
                print(player2name + ' won this round! Good Job!')
                p2score += 1
                break
        print("The scores are: " + player1name + ": " + str(p1score) + " vs " + player2name + ": " + str(p2score))
        answer4 = input("\nChoose from the selected options: \n1. Play again \n2. Return to main menu \n\nEnter option: ")
        clear()
        reset()
        print('\nWelcome to Tic Tac Toe!\n')
        printBoard(board)
        if answer4 == '1':
            x = 0
        else:
            break

"""
1. Gets user to input their name.
2. Prints board.
3. If the board is not full, it loops until either the player or ai wins, or there is a draw.
4. If the letter 'O' has met the conditions to win, print AI has won.
5. If the letter 'X' has met the conditions to win, print players name has won.
6. If there are no moves left to make, print 'Tie Game!'.
"""
def ai():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not (isBoardFull(board)):
        if not (WinCondition(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('The AI won this time!')
            break

        if not (WinCondition(board, 'X')):
            move = compMove()
            if move == 0:
                print('\nTie Game!')
            else:
                LetterPosition('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print(player1name + ' won this round! Good Job!')
            break


"""
1. Loop continues to execute the game until the user decides to exit (inputting n).
2. User chooses whether they would rather play against another player or AI.
2a. If AI, user enters their name and then they go straight into game.
2b. If vs another player, enter both of their names and then they go straight into a game.
3. Prints out the board and then executes the game.
"""
while True:
    print('\nWelcome to the main menu of Tic-Tac Toe ')
    answer2 = input('\nChoose from the selected options: \n1. Player vs Player \n2. vs Computer \n3. Instructions \n4. Exit \n\nEnter option: ')
    if answer2 == '1' or answer2.lower() == 'player' or answer2.lower() == 'pvp':
        board = [' ' for x in range(10)]
        player()
        print('-----------------------------')
        pvp()
    elif answer2 == '2' or answer2.lower() == 'ai' or answer2.lower() == 'computer':
        board = [' ' for x in range(10)]
        player()
        print('-----------------------------')
        ai()
    elif answer2 == '3' or answer2.lower() == 'instructions':
        boardInstructions()
        answer3 = input('\nWould you like to see an example? (y/n): ')
        if answer3.lower() == 'y' or answer3.lower() == 'yes':
            Example()
    elif answer2 == '4' or answer2.lower() == 'exit':
        break
