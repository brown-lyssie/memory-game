from MemoryGame import MemoryGame
from Player import Player
def main():
  player1 = Player("Player 1")
  player2 = Player("Player 2")
  game = MemoryGame(player1, player2)
  game.initiate_board()
  while (True):
    # get whether you want to start
    wannaPlay = input("Do you want to play a game of memory? (y/n)")
    if wannaPlay == "n":
      return
    elif wannaPlay != "y": # not "y", not "n"
      print("Please type y or n.")
      continue
    else: # if "y", move on to next while loop
      break
  print("Welcome to Memory!")
  print("Select the dimensions of your memory game. Max size is 52 total cards (26 pairs of letters)")
  while (True):
    # get whether you want to start
    try:
      lengthStr = input("Select a length.")
      widthStr = input("Select a width.")
      try:
        length = int(lengthStr)
        width = int(widthStr)
        game.set_dimensions(length, width)
        break
      except ValueError as e:
        print(str(e))
        print("Select a valid set of dimensions.")
    except ValueError as e:
      print(str(e))
      print("Select a valid set of dimensions.")
  game.initiate_board()
  while (not game.game_is_over):
    print(game.get_displayed_board_string())
    print(f"{game.players[game.current_player_index].name}, guess two locations.")
    x1Str = input("X for the first guess:")
    y1Str = input("Y for the first guess:")
    x2Str = input("X for the second guess:")
    y2Str = input("Y for the second guess:")
    try:
      x1 = int(x1Str)
      y1 = int(y1Str)
      x2 = int(x2Str)
      y2 = int(y2Str)
      successful_guess = game.pick_two(x1, y1, x2, y2)
      if (successful_guess):
        print("You guessed successfully!")
      else:
        print(game.get_displayed_board_string_with_guesses(x1, y1, x2, y2))
        print("You didn't guess correctly!")
    except ValueError as e:
      print(str(e))
      print("Select a valid pair of points.")
  print(game.get_displayed_board_string())
  if (game.tie):
    print("Both players tied!")
  else:
    print(f"{game.winner.name} won!")
    print(f"Their letters are {', '.join(game.winner.letters)}")
  
  print("Thanks for playing Memory!")

      

if __name__ == "__main__":
  main()
