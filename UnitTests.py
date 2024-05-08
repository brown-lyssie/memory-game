import unittest

from MemoryGame import MemoryGame
from Player import Player

class PlayerUnitTests(unittest.TestCase):
  def testInit(self):
    player = Player("Lyssie")
    self.assertEqual(player.name, "Lyssie")
    self.assertEqual(player.letters, set())
  def testPlayerAddLetter(self):
    player = Player("Lyssie")
    player.add_letter("A")
    testSet = set()
    testSet.add("A")
    self.assertEqual(testSet, player.letters)
    player.add_letter("B")
    testSet.add("B")
    self.assertEqual(testSet, player.letters)
    self.assertRaises(ValueError, player.add_letter, "A")

class MemoryGameUnitTests(unittest.TestCase):
  def testInit(self):
    player1 = Player("Lyssie")
    player2 = Player("Liam")
    game = MemoryGame(player1, player2)
    self.assertEqual(game.length, 3)
    self.assertEqual(game.width, 2)
    self.assertEqual(game.current_player_index, 0)
    self.assertEqual(game.board, [["-", "-"], ["-", "-"]])
    self.assertEqual(game.displayed_board, [["-", "-"], ["-", "-"]])
    self.assertEqual(game.revealed_locations, [])
    self.assertFalse(game.game_is_over)
  def testSetDimensions(self):
    player1 = Player("Lyssie")
    player2 = Player("Liam")
    game = MemoryGame(player1, player2)
    game.set_dimensions(3,4)
    self.assertEqual(game.length, 3)
    self.assertEqual(game.width, 4)
    self.assertEqual(game.board, [["-", "-", "-", "-"], ["-", "-", "-", "-"], ["-", "-", "-", "-"]])
    self.assertEqual(game.displayed_board, [["-", "-", "-", "-"], ["-", "-", "-", "-"], ["-", "-", "-", "-"]])
    self.assertRaises(ValueError, game.set_dimensions, 0, 0)
    self.assertRaises(ValueError, game.set_dimensions, 0, 2)
    self.assertRaises(ValueError, game.set_dimensions, 2, 0)
    self.assertRaises(ValueError, game.set_dimensions, -1, 2)
    self.assertRaises(ValueError, game.set_dimensions, 1, -2)
    self.assertRaises(ValueError, game.set_dimensions, 3, 3)
    self.assertRaises(ValueError, game.set_dimensions, 8, 8)
  def testPickTwo(self):
    player1 = Player("Lyssie")
    player2 = Player("Liam")
    game = MemoryGame(player1, player2)
    game.initiate_board()
    # check where the pairs are
    a_locations = []
    b_locations = []
    for w in range(2):
      for l in range(2):
        if game.board[l][w] == "A":
          a_locations.append((w,l))
        else:
          b_locations.append((w,l))
    # pick invalid location
    self.assertRaises(ValueError, game.pick_two, -1, -1, 0, 0)
    # pick wrong location
    self.assertFalse(game.pick_two(a_locations[0][0], a_locations[0][1], b_locations[0][0], b_locations[0][1]))
    # pick right location
    self.assertTrue(game.pick_two(a_locations[0][0], a_locations[0][1], a_locations[1][0], a_locations[1][1]))
    # pick location that's already been guessed
    self.assertRaises(ValueError, game.pick_two, a_locations[0][0], a_locations[0][1], b_locations[0][0], b_locations[0][1])
    # successfully guess b, and then test that game is over
    self.assertTrue(game.pick_two(b_locations[0][0], b_locations[0][1], b_locations[1][0], b_locations[1][1]))
    # check that game is now over and tied
    self.assertTrue(game.game_is_over)
    self.assertTrue(game.tie)
  def testSwapPlayer(self):
    player1 = Player("Lyssie")
    player2 = Player("Liam")
    game = MemoryGame(player1, player2)
    game.swap_player()
    self.assertEqual(game.current_player_index, 1)




if __name__ == "__main__":
  unittest.main()

