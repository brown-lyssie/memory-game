from Player import Player
import random

BLANK_SPOT = "-"
# memory
class MemoryGame:
  def __init__(self, player1, player2):
    self.players = [player1, player2]
    self.winner = None
    self.tie = False
    self.current_player_index = 0
    self.started = False
    self.length = 2
    self.width = 2
    self.board = [["-" for i in range(self.width)] for j in range(self.length)]
    self.displayed_board = [["-" for i in range(self.width)] for j in range(self.length)]
    self.revealed_locations = []
    self.game_is_over = False
    pass
  def set_dimensions(self, length, width):
    if ((length * width) % 2 != 0):
      raise ValueError(f"Cannot set dimensions {length} x {width}, need even number of entries")
    elif (length * width > 26 * 2):
      raise ValueError(f"Cannot set dimensions {length} x {width}, there is only 26 letters in the alphabet")
    elif (length <= 0):
      raise ValueError(f"Cannot set length to {length}, must be a positive number")
    elif (width <= 0):
      raise ValueError(f"Cannot set width to {width}, must be a positive number")
    else:
      self.length = length
      self.width = width
      self.board = [[BLANK_SPOT for i in range(width)] for j in range(length)]
      self.displayed_board = [[BLANK_SPOT for i in range(width)] for j in range(length)]
  def pick_two(self, x1, y1, x2, y2):
    if (x1 >= self.width or x1 < 0) or \
       (x2 >= self.width or x2 < 0) or \
       (y1 >= self.length or y1 < 0) or \
       (y2 >= self.length or y2 < 0):
      raise ValueError("Dimensions out of bounds!")
    if ((x1, y1) in self.revealed_locations or (x2, y2) in self.revealed_locations):
      raise ValueError("Already guessed this location!")
       
    val1 = self.board[y1][x1]
    val2 = self.board[y2][x2]
    # correct guess
    if (val1 == val2 and val1 != BLANK_SPOT):
      self.players[self.current_player_index].add_letter(val1)
      self.displayed_board[y1][x1] = val1
      self.displayed_board[y2][x2] = val1
      self.revealed_locations.append((x1, y1))
      self.revealed_locations.append((x2, y2))
      # if all locations have been revealed
      if (len(self.revealed_locations) == self.length * self.width):
        self.handle_end_of_game()
        return True
      else:
        self.swap_player()
      return True
    else:
      self.swap_player()
      return False
  def initiate_board(self):
    num_valid_locations = self.length * self.width
    num_letters = num_valid_locations // 2
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # build list of valid ordered pairs
    valid_locations = []
    for y in range(self.length):
      for x in range(self.width):
        valid_locations.append((x,y))
    # for each letter, select two random locations to replace the letters with
    for i in range(num_letters):
      for p in range(2):
        location = random.choice(valid_locations)
        valid_locations.remove(location)
        self.board[location[1]][location[0]] = letters[i]
  def get_displayed_board_string(self):
    display_str = ""
    for row in self.displayed_board:
      display_str += " ".join(row)
      display_str += "\n"
    return display_str
  def get_displayed_board_string_with_guesses(self, x1, y1, x2, y2):
    # copy list
    displayed_board_with_guesses = []
    for row in self.displayed_board:
      displayed_board_with_guesses.append([])
      for val in row:
        displayed_board_with_guesses[-1].append(val)
    displayed_board_with_guesses[y1][x1] = self.board[y1][x1]
    displayed_board_with_guesses[y2][x2] = self.board[y2][x2]
    display_str = ""
    for row in displayed_board_with_guesses:
      display_str += " ".join(row)
      display_str += "\n"
    return display_str
  def swap_player(self):
    if self.current_player_index == 1:
      self.current_player_index = 0
    else:
      self.current_player_index = 1
  def handle_end_of_game(self):
    if (len(self.players[0].letters) > len(self.players[1].letters)):
      self.winner = self.players[0]
    elif (len(self.players[1].letters) > len(self.players[0].letters)):
      self.winner = self.players[1]
    else:
      self.winner = self.players
      self.tie = True
    self.game_is_over = True