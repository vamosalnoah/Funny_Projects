import os
import game_art
import game_data

def show_game_board(matrix):
    hr = "----------------"
    for row in matrix:
        print (hr)

        line = ""
        for x in list(row):
            line += f"  {x}  |"
        print(line[:-1])

    print(hr)


def update_game_board(flag, pos):
    if flag:
        marker = "O"
    else:
        marker = "X"

    global current_game_board

    matrix_pos = game_data.game_board_position[pos]

    if current_game_board[matrix_pos] != " ":
        return False
    
    current_game_board[matrix_pos] = marker
    return True


def player(flag):
    if not flag:
        return "Jugador A"
    if flag:
        return "Jugador B"
    

def player_win_art(flag):
    if not flag:
        return game_art.player_A_wins_art
    if flag:
        return game_art.player_B_wins_art
    

def is_there_a_winner():
    global current_game_board

    for row in game_data.winning_combos:

        if current_game_board[row[0]] != " " and \
            current_game_board[row[0]] == current_game_board[row[1]] and \
            current_game_board[row[0]] == current_game_board[row[2]]:
            return True
        
    return False

def is_a_gato():
    global current_game_board

    for row in current_game_board:
        for x in list(row):
            if x == " ":
                return False
            
    return True

def end_current_game(gato=False):
    show_game_board(current_game_board)

    global player_flag
    if not gato:
        print(f"{player_win_art(player_flag)}")
    if gato:
        print(f"{game_art.gato_art}")


    global game_on
    game_on = False

    input("Presiona cualquier tecla para continuar...")


# Start game
current_game_board = game_data.game_board


while True:
    game_on = True
    player_flag = False

    os.system('cls')

    print(game_art.welcome_art)
    print("Estas son las posiciones del tablero:")
    show_game_board(game_data.game_positions)

    ans = input("Presiona cualquier tecla para continuar, 'q' para salir: ")

    if ans.lower() == "q":
        break

    while game_on:
        while True:
            show_game_board(current_game_board)
            position = int(input(f"{player(player_flag)}: Elige posición: "))

            success = update_game_board(player_flag, position)

            if success:
                break
            else:
                print("¡Posición ocupada!")

        if is_there_a_winner():
            end_current_game()
        elif is_a_gato():
            end_current_game(True)

        player_flag = not player_flag