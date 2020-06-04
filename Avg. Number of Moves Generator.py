import random
import os
import subprocess

# main() only outputs data to console
def main():
    
    # returns data
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

        # runs 10 games
        for x in range (10):

            print("\nNew Game\n")
                
            # chess board re-initialized at start of each game since I re-define class chess below (though of course re-defining it isn't really necessary)
            import chess
            board = chess.Board()

            repeat_moves = 0
            total_moves = 0
            moves_list = []
            checkmates = 0

            class chess:
                    def num_moves(legal_moves):
                            num_moves = str(legal_moves)
                            # for formatting reasons list of legal_moves is made string and sliced
                            num_moves = num_moves [38:-2]
                            num_moves = num_moves.split(",")
                            return len(num_moves), num_moves

            while board.is_checkmate() == False:
                # chess.num_moves returns formatted string rendition of legal move list
                list_moves = chess.num_moves(board.legal_moves) [1]
                # total_moves increments each iteration
                total_moves = move_counter(list_moves, total_moves)
                # randomly selects from list of legal_moves
                next_move = random.choice(list_moves)
                # formats list elements so that string is acceptable perameter to board.push_san
                next_move = next_move.strip(" ")
                print(next_move)
                moves_list.append(next_move)
                board.push_san(next_move)

                # accommodates checkmates
                if "#" in next_move:
                      checkmates += 1
                      break
                      
                # shuts down game if each opponent has played 200 or more turns
                if len(moves_list) / 2 >= 200:
                        break

            for move_num in range (len(moves_list)-4):
                # is considered repeat if turn before last is same-
                # (i.e. moving from one square next turn, then subsequent turn moving back to same square)
                    if (moves_list[0 + move_num]) == (moves_list[4 + move_num]):
                            repeat_moves += 1
# vanilla exception catch
    except Exception as error:
        print(error)

    return total_moves, repeat_moves, moves_list, checkmates

main()
