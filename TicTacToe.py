# 0 -empy
# 1 - player1
# 2 - player2
import sys

state = [ 0, 0, 0, 0, 0, 0, 0, 0, 0]

#--------------------------------FUNTIONS---------------------------------------

def print_state(state):
    global a
    a = []
    for item in state:
        if item == 0:
            a.append(" ")
        elif item == 1:
            a.append("X")
        elif item == 2:
            a.append("O")

    return

def print_map():
    print(f"|{a[0]}|{a[1]}|{a[2]}|")
    print(f"|{a[3]}|{a[4]}|{a[5]}|")
    print(f"|{a[6]}|{a[7]}|{a[8]}|")

    return

def turn_p1():
    global player1
    while True:
        player1 = int(input("Player One chooses position(1-9): "))
        if player1 == 1 and state[0] == 0 and state[0] != 2:
            state[0] = 1
        elif player1 == 2 and state[1] == 0 and state[1] != 2:
            state[1] = 1
        elif player1 == 3 and state[2] == 0 and state[2] != 2:
            state[2] = 1
        elif player1 == 4 and state[3] == 0 and state[3] != 2:
            state[3] = 1
        elif player1 == 5 and state[4] == 0 and state[4] != 2:
            state[4] = 1
        elif player1 == 6 and state[5] == 0 and state[5] != 2:
            state[5] = 1
        elif player1 == 7 and state[6] == 0 and state[6] != 2:
            state[6] = 1
        elif player1 == 8 and state[7] == 0 and state[7] != 2:
            state[7] = 1
        elif player1 == 9 and state[8] == 0 and state[8] != 2:
            state[8] = 1
        else:
            player1 = int(player1)

        if player1 in range(1,10):
            break

    print_state(state)
    print_map()

    return

def turn_p2():
    global player2
    while True:
        player2 = int(input("Player Two chooses position(1-9): "))
        if player2 == 1 and state[0] == 0 and state[0] != 1:
            state[0] = 2
        elif player2 == 2 and state[1] == 0 and state[1] != 1:
            state[1] = 2
        elif player2 == 3 and state[2] == 0 and state[2] != 1:
            state[2] = 2
        elif player2 == 4 and state[3] == 0 and state[3] != 1:
            state[3] = 2
        elif player2 == 5 and state[4] == 0 and state[4] != 1:
            state[4] = 2
        elif player2 == 6 and state[5] == 0 and state[5] != 1:
            state[5] = 2
        elif player2 == 7 and state[6] == 0 and state[6] != 1:
            state[6] = 2
        elif player2 == 8 and state[7] == 0 and state[7] != 1:
            state[7] = 2
        elif player2 == 9 and state[8] == 0 and state[8] != 1:
            state[8] = 2
        else:
            player2 = int(player2)

        if player2 in range(1,10):
            break

    print_state(state)
    print_map()

    return

def win():
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

#------------------------------GAME---------------------------------------------

while True:
    while True:
        turn_p1()

        if win() == 1:
            print("Player One wins!")
            break

        turn_p2()

        if win() == 2:
            print("Player Two wins!")
            break

    finish = int(input("Game finished, choose 1 to play another game, or 2 to exit: "))
    if finish == 1:
        continue
    elif finish == 2:
        sys.exit("Leaving the game...")
