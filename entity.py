#Kent Tran, Matthew Trinh
#Group 4
#October 7, 2025
#Dragon Trainer

class Entity:
  """
  Base cass for all entities
  Attributes: name (string): name of the entity
              max_hp (int): maximum health points of the entity
              hp (int): current health points of the entity
  """
  def __init__(self, name, max_hp):
    """
    Initializes the entity with name, max health, and current health

    Args: name (string): name of the entity
          max_hp (int): maximum health points of the entity
    """
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp

  @property
  def name(self):
    return self._name

  @property
  def hp(self):
    return self._hp

  def take_damage(self, damage):
    """
    Decreases the entity's health by the specified amount
    
    Args: damage (int): amount of damage the dragon takes
    """
    self._hp -= damage
    if self._hp < 0:
      self._hp = 0

  def __str__(self):
    """
    Returns a string representation of the entity
    
    Args: None
    """
    return self.name + ": " + str(self.hp) + "/" + str(self._max_hp)