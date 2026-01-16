#Kent Tran, Matthew Trinh
#Group 4
#October 7, 2025
#Dragon Trainer

import random
from dragon import Dragon

class Flying(Dragon):
  def __init__(self, name, hp):
    """
    Call the super to set the dragon's name and hp, assign a default number of swoops
    
    Args: name (string): the dragon's name
          hp (int): the dragon's hit points
          
    Returns: None
    """
    super().__init__(name, hp)
    self._swoops = 2

  def special_attack(self, hero):
    """
    Overriden swoop attack: if the dragon has any swoops left, apply a random amount of damage to the hero,
    decrement the number of swoops, and return a string describing the attack. Otherwise, deal no damage and
    return a string describing the lack of swoops.
    
    Args: hero (Hero): the hero to attack
    
    Returns: A string describing the damage done from the attack
    """
    if self._swoops > 0:
      damage = random.randint(5, 8)
      hero.take_damage(damage)
      self._swoops -= 1
      return self.name + " swoops down and bites you for " + str(damage) + " damage!"
    else:
      return self.name + " tries to swoop down, but has no swoops left!"

  def __str__(self):
    """
    Use the superclass's __str__ from entity, then concatenate the number of swoops
    """
    return super().__str__() + "\nSwoop attacks remaining: " + str(self._swoops)