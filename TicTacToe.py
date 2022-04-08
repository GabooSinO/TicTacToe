# 0 - empy
# 1 - player1
# 2 - player2
state = [ 0, 0, 0, 0, 0, 0, 0, 0, 0]

#--------------------------------FUNTIONS---------------------------------------

def print_state(state):
    a = []
    for item in state:
        if item == 0:
            a.append(" ")
        elif item == 1:
            a.append("X")
        elif item == 2:
            a.append("O")

    print(f"|{a[0]}|{a[1]}|{a[2]}|")
    print(f"|{a[3]}|{a[4]}|{a[5]}|")
    print(f"|{a[6]}|{a[7]}|{a[8]}|")

def turn_p1():
    while True:
        try:
            player1 = int(input("Player One chooses position(1-9): "))
        except Exception:
            continue    # If it cant convert it to int, ask again

        # Check if the player's input is out of range
        if player1 not in range(1,10):
            print("Wrong input! Try again...")
            continue

        # Set the cell state if the cell is empty
        if state[player1-1] == 0:
            state[player1-1] = 1
        else:
            print(f"Place {player1} is taken by Player {state[player1-1]}! Try again...")
            continue

        print_state(state)
        if check_win():
            print("Player 1 wins!")
            return True     # Wins
        return False

def turn_p2():
    while True:
        try:
            player2 = int(input("Player Two chooses position(1-9): "))
        except Exception:
            continue

        if player2 not in range(1,10):
            print("Wrong input! Try again...")
            continue

        if state[player2-1] == 0:
            state[player2-1] = 2
        else:
            print(f"Place {player2} is taken by Player {state[player2-1]}! Try again...")
            continue

        print_state(state)
        if check_win():
            print("Player 2 wins!")
            return True
        return False

def check_win():
    # You only need to check the cross
    for n in state:
        if (n in [1,4,7]) and (state[n-1] == state[n] == state[n+1]):       # Horizontal
            return True
        elif (n in [3,4,5]) and (state[n-3] == state[n] == state[n+3]):     # Vertical
            return True
        elif (n == 4) and (state[0] == state[n] == state[8] or state[2] == state[n] == state[6]):                               # Diagonal
            return True
        else:
            return False

    """
    if ((state[0]==state[1]==state[2]) and state[0]== 1) or (state[3]==state[4]==state[5] and state[3]== 1) or ((state[6]==state[7]==state[8]) and state[6]== 1):
        return 1
    elif ((state[0]==state[1]==state[2]) and state[0]== 2 ) or ((state[3]==state[4]==state[5]) and state[3]== 2) or ((state[6]==state[7]==state[8]) and state[6]== 2):
        return 2
    elif ((state[0]==state[3]==state[6]) and state[0]== 1) or ((state[1]==state[4]==state[7]) and state[1]== 1) or ((state[2]==state[5]==state[8]) and state[2]== 1):
        return 1
    elif((state[0]==state[3]==state[6]) and state[0]== 2) or ((state[1]==state[4]==state[7]) and state[1]== 2) or ((state[2]==state[5]==state[8]) and state[2]== 2):
        return 2
    elif (state[0]==state[4]==state[8] or state[2]==state[4]==state[6] ) and  state[4]== 1:
        return 1
    elif (state[0]==state[4]==state[8] or state[2]==state[4]==state[6] ) and  state[4]== 2:
        return 2
    else:
        return 0
    """

#------------------------------------GAME------------------------------------------

while True:
    count = 0   # Count the number of steps
    while True:
        if count < 8:
            if turn_p1():   # P1 wins
                break
        if count < 9:
            if turn_p2():   # P2 wins
                break
        else:
            print("Tie!")
            break
        count += 2          # 2 turns / loop

    finish = int(input("Game finished, choose 1 to play another game, or 2 to exit: "))
    if finish == 1:
        state = [ 0, 0, 0, 0, 0, 0, 0, 0, 0] 
        print("Starting new game...")
    else:
        exit("Leaving the game...")

