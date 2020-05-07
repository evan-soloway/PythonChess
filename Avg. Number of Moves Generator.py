import random
import os
import subprocess

def main():
    
    total_moves, repeat_moves, moves_list, checkmates = auto_game_player()

    print("\nTotal number of potential moves for each turn of each player \
through most recent game:", total_moves)

    print("\nAverage number of potential moves for each turn of each player \
through most recent game:", int(total_moves / len(moves_list)))

    print("\nNumber of repeat moves overall between both players through most recent game:", repeat_moves) 

    print("\nNumber of checkmates:", checkmates)

    print("\nList of moves:\n\n", *moves_list)

    subprocess.Popen("start https://www.chess.com/analysis", shell=True)
    
def move_counter(current_move_turns, total_moves):
    total_moves += len(current_move_turns)
    return total_moves

def auto_game_player():

    try:

        for x in range (10):

            print("\nNew Game\n")
                
            import chess
            board = chess.Board()

            repeat_moves = 0
            total_moves = 0
            moves_list = []
            checkmates = 0

            class chess:
                    def num_moves(legal_moves):
                            num_moves = str(legal_moves)
                            num_moves = num_moves [38:-2]
                            num_moves = num_moves.split(",")
                            return len(num_moves), num_moves

            while board.is_checkmate() == False:
                list_moves = chess.num_moves(board.legal_moves) [1]
                total_moves = move_counter(list_moves, total_moves)
                next_move = random.choice(list_moves)
                next_move = next_move.strip(" ")
                print(next_move)
                moves_list.append(next_move)
                board.push_san(next_move)

                if "#" in next_move:
                      checkmates += 1
                      break
                      
                if len(moves_list) / 2 >= 200:
                        break

            for move_num in range (len(moves_list)-4):
                    if (moves_list[0 + move_num]) == (moves_list[4 + move_num]):
                            repeat_moves += 1

    except Exception as error:
        print(error)

    return total_moves, repeat_moves, moves_list, checkmates

main()
