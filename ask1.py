# libraries
import random


# functions
def emptyBoard():
    print("============================================= OTRIO GAME =============================================")
    print("This is an empty board that needs to be filled with rings, of different sizes..")

    board3D = [[['______' for ring in range(3)] for col in range(3)] for row in range(3)]

    print("                    Col.1:                          Col.2:                          Col.3:")
    for i in range(3):
        print(f'Row {i + 1}:', board3D[i])
    print("-------------------------------------------- Let's play!! --------------------------------------------")

    rings = ['small', 'medium', 'large']
    small_rings = ['small', 'small', 'small', 'small', 'small', 'small', 'small', 'small', 'small']
    medium_rings = ['medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium']
    large_rings = ['large', 'large', 'large', 'large', 'large', 'large', 'large', 'large', 'large']

    return rings, small_rings, medium_rings, large_rings, board3D


def randomChoiceSize(rings, board3D):
    tmp1 = random.choice(rings)
    while True:
        if tmp1 == 'small':
            if (board3D[0][0][0] != 'small' or board3D[0][1][0] != 'small' or board3D[0][2][0] != 'small') or \
                    (board3D[1][0][0] != 'small' or board3D[1][1][0] != 'small' or board3D[1][2][0] != 'small') or \
                    (board3D[2][0][0] != 'small' or board3D[2][1][0] != 'small' or board3D[2][2][0] != 'small'):
                size_choice = tmp1
                break
        elif tmp1 == 'medium':
            if (board3D[0][0][1] != 'medium' or board3D[0][1][1] != 'medium' or board3D[0][2][1] != 'medium') or \
                    (board3D[1][0][1] != 'medium' or board3D[1][1][1] != 'medium' or board3D[1][2][1] != 'medium') or \
                    (board3D[2][0][1] != 'medium' or board3D[2][1][1] != 'medium' or board3D[2][2][1] != 'medium'):
                size_choice = tmp1
                break
        elif tmp1 == 'large':
            if (board3D[0][0][2] != 'large' or board3D[0][1][2] != 'large' or board3D[0][2][2] != 'large') or \
                    (board3D[1][0][2] != 'large' or board3D[1][1][2] != 'large' or board3D[1][2][2] != 'large') or \
                    (board3D[2][0][2] != 'large' or board3D[2][1][2] != 'large' or board3D[2][2][2] != 'large'):
                size_choice = tmp1
                break
        tmp1 = random.choice(rings)
    return size_choice


def randomChoicePosition(size_choice, board3D, small_rings, medium_rings, large_rings):
    tmp2 = (random.randint(0, 2), random.randint(0, 2))
    while True:
        if size_choice == 'small':
            if tmp2 == (0, 0):
                if board3D[0][0][0] != 'small' and small_rings:
                    board3D[0][0][0] = small_rings.pop()
                    break
            elif tmp2 == (0, 1):
                if board3D[0][1][0] != 'small' and small_rings:
                    board3D[0][1][0] = small_rings.pop()
                    break
            elif tmp2 == (0, 2):
                if board3D[0][2][0] != 'small' and small_rings:
                    board3D[0][2][0] = small_rings.pop()
                    break
            elif tmp2 == (1, 0):
                if board3D[1][0][0] != 'small' and small_rings:
                    board3D[1][0][0] = small_rings.pop()
                    break
            elif tmp2 == (1, 1):
                if board3D[1][1][0] != 'small' and small_rings:
                    board3D[1][1][0] = small_rings.pop()
                    break
            elif tmp2 == (1, 2):
                if board3D[1][2][0] != 'small' and small_rings:
                    board3D[1][2][0] = small_rings.pop()
                    break
            elif tmp2 == (2, 0):
                if board3D[2][0][0] != 'small' and small_rings:
                    board3D[2][0][0] = small_rings.pop()
                    break
            elif tmp2 == (2, 1):
                if board3D[2][1][0] != 'small' and small_rings:
                    board3D[2][1][0] = small_rings.pop()
                    break
            elif tmp2 == (2, 2):
                if board3D[2][2][0] != 'small' and small_rings:
                    board3D[2][2][0] = small_rings.pop()
                    break
        elif size_choice == 'medium':
            if tmp2 == (0, 0):
                if board3D[0][0][1] != 'medium' and medium_rings:
                    board3D[0][0][1] = medium_rings.pop()
                    break
            elif tmp2 == (0, 1):
                if board3D[0][1][1] != 'medium' and medium_rings:
                    board3D[0][1][1] = medium_rings.pop()
                    break
            elif tmp2 == (0, 2):
                if board3D[0][2][1] != 'medium' and medium_rings:
                    board3D[0][2][1] = medium_rings.pop()
                    break
            elif tmp2 == (1, 0):
                if board3D[1][0][1] != 'medium' and medium_rings:
                    board3D[1][0][1] = medium_rings.pop()
                    break
            elif tmp2 == (1, 1):
                if board3D[1][1][1] != 'medium' and medium_rings:
                    board3D[1][1][1] = medium_rings.pop()
                    break
            elif tmp2 == (1, 2):
                if board3D[1][2][1] != 'medium' and medium_rings:
                    board3D[1][2][1] = medium_rings.pop()
                    break
            elif tmp2 == (2, 0):
                if board3D[2][0][1] != 'medium' and medium_rings:
                    board3D[2][0][1] = medium_rings.pop()
                    break
            elif tmp2 == (2, 1):
                if board3D[2][1][1] != 'medium' and medium_rings:
                    board3D[2][1][1] = medium_rings.pop()
                    break
            elif tmp2 == (2, 2):
                if board3D[2][2][1] != 'medium' and medium_rings:
                    board3D[2][2][1] = medium_rings.pop()
                    break
        elif size_choice == 'large':
            if tmp2 == (0, 0):
                if board3D[0][0][2] != 'large' and large_rings:
                    board3D[0][0][2] = large_rings.pop()
                    break
            elif tmp2 == (0, 1):
                if board3D[0][1][2] != 'large' and large_rings:
                    board3D[0][1][2] = large_rings.pop()
                    break
            elif tmp2 == (0, 2):
                if board3D[0][2][2] != 'large' and large_rings:
                    board3D[0][2][2] = large_rings.pop()
                    break
            elif tmp2 == (1, 0):
                if board3D[1][0][2] != 'large' and large_rings:
                    board3D[1][0][2] = large_rings.pop()
                    break
            elif tmp2 == (1, 1):
                if board3D[1][1][2] != 'large' and large_rings:
                    board3D[1][1][2] = large_rings.pop()
                    break
            elif tmp2 == (1, 2):
                if board3D[1][2][2] != 'large' and large_rings:
                    board3D[1][2][2] = large_rings.pop()
                    break
            elif tmp2 == (2, 0):
                if board3D[2][0][2] != 'large' and large_rings:
                    board3D[2][0][2] = large_rings.pop()
                    break
            elif tmp2 == (2, 1):
                if board3D[2][1][2] != 'large' and large_rings:
                    board3D[2][1][2] = large_rings.pop()
                    break
            elif tmp2 == (2, 2):
                if board3D[2][2][2] != 'large' and large_rings:
                    board3D[2][2][2] = large_rings.pop()
                    break
        tmp2 = (random.randint(0, 2), random.randint(0, 2))
    return board3D, small_rings, medium_rings, large_rings


def victoryCheck(board3D):
    win = False

    # horizontal check
    if (board3D[0][0][0] == board3D[0][1][0] == board3D[0][2][0] == 'small' or
        board3D[0][0][1] == board3D[0][1][1] == board3D[0][2][1] == 'medium' or
        board3D[0][0][2] == board3D[0][1][2] == board3D[0][2][2] == 'large') or \
            ((board3D[0][0][0] == 'small' and board3D[0][1][1] == 'medium' and board3D[0][2][2] == 'large') or
             (board3D[0][2][0] == 'small' and board3D[0][1][1] == 'medium' and board3D[0][0][2] == 'large')):
        win = True
        return win
    elif (board3D[1][0][0] == board3D[1][1][0] == board3D[1][2][0] == 'small' or
          board3D[1][0][1] == board3D[1][1][1] == board3D[1][2][1] == 'medium' or
          board3D[1][0][2] == board3D[1][1][2] == board3D[1][2][2] == 'large') or \
            ((board3D[1][0][0] == 'small' and board3D[1][1][1] == 'medium' and board3D[1][2][2] == 'large') or
             (board3D[1][2][0] == 'small' and board3D[1][1][1] == 'medium' and board3D[1][0][2] == 'large')):
        win = True
        return win
    elif (board3D[2][0][0] == board3D[2][1][0] == board3D[2][2][0] == 'small' or
          board3D[2][0][1] == board3D[2][1][1] == board3D[2][2][1] == 'medium' or
          board3D[2][0][2] == board3D[2][1][2] == board3D[2][2][2] == 'large') or \
            ((board3D[2][0][0] == 'small' and board3D[2][1][1] == 'medium' and board3D[2][2][2] == 'large') or
             (board3D[2][2][0] == 'small' and board3D[2][1][1] == 'medium' and board3D[2][0][2] == 'large')):
        win = True
        return win

    # vertical check
    if (board3D[0][0][0] == board3D[1][0][0] == board3D[2][0][0] == 'small' or
        board3D[0][0][1] == board3D[1][0][1] == board3D[2][0][1] == 'medium' or
        board3D[0][0][2] == board3D[1][0][2] == board3D[2][0][2] == 'large') or \
            ((board3D[0][0][0] == 'small' and board3D[1][0][1] == 'medium' and board3D[2][0][2] == 'large') or
             (board3D[2][0][0] == 'small' and board3D[1][0][1] == 'medium' and board3D[0][0][2] == 'large')):
        win = True
        return win
    elif (board3D[0][1][0] == board3D[1][1][0] == board3D[2][1][0] == 'small' or
          board3D[0][1][1] == board3D[1][1][1] == board3D[2][1][1] == 'medium' or
          board3D[0][1][2] == board3D[1][1][2] == board3D[2][1][2] == 'large') or \
            ((board3D[0][1][0] == 'small' and board3D[1][1][1] == 'medium' and board3D[2][1][2] == 'large') or
             (board3D[2][1][0] == 'small' and board3D[1][1][1] == 'medium' and board3D[0][1][2] == 'large')):
        win = True
        return win
    elif (board3D[0][2][0] == board3D[1][2][0] == board3D[2][2][0] == 'small' or
          board3D[0][2][1] == board3D[1][2][1] == board3D[2][2][1] == 'medium' or
          board3D[0][2][2] == board3D[1][2][2] == board3D[2][2][2] == 'large') or \
            ((board3D[0][2][0] == 'small' and board3D[1][2][1] == 'medium' and board3D[2][2][2] == 'large') or
             (board3D[2][2][0] == 'small' and board3D[1][2][1] == 'medium' and board3D[0][2][2] == 'large')):
        win = True
        return win

    # diagonal check
    if (board3D[0][0][0] == board3D[1][1][0] == board3D[2][2][0] == 'small' or
        board3D[0][0][1] == board3D[1][1][1] == board3D[2][2][1] == 'medium' or
        board3D[0][0][2] == board3D[1][1][2] == board3D[2][2][2] == 'large') or \
            ((board3D[0][0][0] == 'small' and board3D[1][1][1] == 'medium' and board3D[2][2][2] == 'large') or
             (board3D[2][2][0] == 'small' and board3D[1][1][1] == 'medium' and board3D[0][0][2] == 'large')):
        win = True
        return win
    elif (board3D[2][0][0] == board3D[1][1][0] == board3D[0][2][0] == 'small' or
          board3D[2][0][1] == board3D[1][1][1] == board3D[0][2][1] == 'medium' or
          board3D[2][0][2] == board3D[1][1][2] == board3D[0][2][2] == 'large') or \
            ((board3D[2][0][0] == 'small' and board3D[1][1][1] == 'medium' and board3D[0][2][2] == 'large') or
             (board3D[0][2][0] == 'small' and board3D[1][1][1] == 'medium' and board3D[2][0][2] == 'large')):
        win = True
        return win

    return win


# main code
t = emptyBoard()  # creates & prints an empty board and creates all the necessary lists for the rings
rings = t[0];  small_rings = t[1];  medium_rings = t[2];  large_rings = t[3];  board3D = t[4]

sum_moves = 0  # total number of random moves for 100 otrio games
for game in range(100):
    ring_count = 0  # number of rings placed on the board / number of rounds for each game
    flag = False

    while ring_count < 27:
        if not flag:  # if the game hasn't ended
            size_choice = randomChoiceSize(rings, board3D) # random choice for ring size
            randomChoicePosition(size_choice, board3D, small_rings, medium_rings, large_rings) # random choice for ring's position

            print("\n")
            print("                    Col.1:                          Col.2:                          Col.3:")
            for i in range(3):
                print(f'Row {i + 1}:', board3D[i]) # documents game's progress

            flag = victoryCheck(board3D)  # searches for winning move (horizontally, vertically and diagonally etc.)
            if flag:
                print(f"AI won, on round {ring_count + 1}!")
                print("\n")
                t = emptyBoard()
                rings = t[0];  small_rings = t[1];  medium_rings = t[2];  large_rings = t[3];  board3D = t[4]
                break
            elif not flag and ring_count >= 2:
                print(f"No winning match found, on round {ring_count + 1}.")
            else:
                print("Win cannot be determined yet, because the number of rings is less than 3...")

        ring_count += 1

    sum_moves += ring_count

print("\n")
MO = sum_moves / 100  # calculates the average amount of moves needed to win otrio
print("Average number of moves to win this game:", MO)
