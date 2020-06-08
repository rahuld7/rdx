import itertools
import pyfiglet
from colorama import init, Fore

def banner():
    ascii_banner = pyfiglet.figlet_format("TIC-TAC-TOE")
    print(Fore.BLUE + ascii_banner)
    #print(Fore.RED + "by RDX")


def win(current_game):

    def decide(check, M):
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(Fore.YELLOW + "winner")
            #print(check)
            return True
        else:
            return False

    # horizontal
    for row in game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(Fore.YELLOW + "winner")
            #print(row)
            return True
    #vertical
    for col in  range(len(game[0])):
        check_V = []
        for row in game:
            check_V.append(row[col])
        if decide(check_V, "V"):
            return True

    #diagonals
    check_D1 = []
    check_D2 = []
    for i, row in enumerate(game):
        check_D1.append(row[i])
        check_D2.append(row[len(game) - i - 1])
    if decide(check_D1, "D1"):
            return True
    if decide(check_D2, "D2"):
            return True

    return False





def game_board(game_map, player = 0, row = 0, column = 0, just_display = False):
    try:
        if game_map[row][column] != 0:
            print(Fore.RED + "ocupied Choose another!")
            return game_map, False
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count,row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print(Fore.RED + "Try again", e)
        return game_map, False
    except Exception as e:
        print(Fore.RED + "something is wrong", e)
        return game_map, False



init(autoreset=True)
play = True
#player = [1, 2]

while play:
    game = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    banner()

    game_won = False
    game, _ = game_board(game, just_display = True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)

        if current_player == 1:
            print(Fore.RED + f"Current Player: {current_player}")
        elif current_player == 2:
            print(Fore.GREEN + f"Current Player: {current_player}")

        played = False

        while not played:
            col_choice = int(input("column: "))
            row_choice = int(input("row: "))
            game, played = game_board(game, current_player, row_choice, col_choice)
        if win(game):
            game_won = True
            again = input("Try again(y/n): ")
            if again.lower() == "y":
                print(Fore.GREEN + "Restarting...........")
            elif again.lower() == "n":
                print(Fore.MAGENTA + "bye")
                play = False
            else:
                print(Fore.RED + "NOT VALID!")
                play = False
