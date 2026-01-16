#Kent Tran, Matthew Trinh
#Group 4
#October 7, 2025
#Dragon Trainer

import random
from entity import Entity

class Hero(Entity):
  """
  Initializes the hero with name, max health, and current health
  Attributes: inherits all attributes from Entity
  """
  def sword_attack(self, dragon):
    """
    Deals random damage to the dragon
    Args: dragon (Dragon): the dragon to attack
    Returns: A string describing the damage done from the attack
    """
    damage = random.randint(1, 6) + random.randint(1, 6)
    dragon.take_damage(damage)
    return "You slash the " + dragon.name + " with your sword for " + str(damage) + " damage."

  def arrow_attack(self, dragon):
    """
    Deals random damage to the dragon
    Args: dragon (Dragon): the dragon to attack
    Returns: A string describing the damage done from the attack
    """
    damage = random.randint(1, 12)
    dragon.take_damage(damage)
    return "You hit the " + dragon.name + " with your arrow for " + str(damage) + " damage."