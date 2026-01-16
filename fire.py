#Kent Tran, Matthew Trinh
#Group 4
#October 7, 2025
#Dragon Trainer

import random
from dragon import Dragon

class Fire(Dragon):
  def __init__(self, name, hp):
    """
    Call super to set the dragon's name and hp, assign a default number of fireballs
    Args: name (string): the dragon's name
          hp (int): the dragon's hit points
    Returns: None
    """
    super().__init__(name, hp)
    self._fire_shots = 3

  def special_attack(self, hero):
    """
    Overidden fire attack: if the dragon has any fire shots left, apply a random amount of damage to the hero,
    decrement the number of fire_shots, and return a string describing the attack. Otherwise, deal no damage and
    return a string describing the lack of fire_shots.
    Args: hero (Hero): the hero to attack
    Returns: A string describing the damage done from the attack
    """
    if self._fire_shots > 0:
      damage = random.randint(6, 9)
      hero.take_damage(damage)
      self._fire_shots -= 1
      return self.name + " engulfs you in flames for " + str(damage) + " damage!"
    else:
      return self.name + " tries to spit fire at you but is all out of fire shots!"

  def __str__(self):
    """
    Use the superclass's __str__ from entity, then concatenate the number of fireballs
    """
    return super().__str__() + "\nFire Shots remaining: " + str(self._fire_shots)