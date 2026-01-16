#Kent Tran, Matthew Trinh
#Group 4
#October 7, 2025
#Dragon Trainer

import random
from entity import Entity

class Dragon(Entity):
  def basic_attack(self, hero):
    """
    Tail attack: heros takes a random amount of damage
    Args: hero (Hero): the hero to attack
    Returns: A string describing the damage done from the attack
    """
    damage = random.randint(2, 5)
    hero.take_damage(damage)
    return self.name + " smashes you with its tail for " + str(damage) + " damage!"

  def special_attack(self, hero):
    """
    Claw attack: heros takes a random amount of damage
    Args: hero (Hero): the hero to attack
    Returns: A string describing the damage done from the attack
    """
    damage = random.randint(3, 7)
    hero.take_damage(damage)
    return self.name + " slashes you with its claws for " + str(damage) + " damage!"