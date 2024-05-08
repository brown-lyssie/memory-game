class Player:
  def __init__(self, name):
    self.name = name
    self.letters = set()
  def add_letter(self, letter):
    if letter in self.letters:
      raise ValueError("Player already has the letter " + letter)
    else:
      self.letters.add(letter)