#Kent Tran, Matthew Trinh
#Group 4
#October 7, 2025
#Dragon Trainer: Defeat 3 dragons to pass the trial in a turn based game

import check_input
import random
from hero import Hero
from dragon import Dragon
from fire import Fire
from flying import Flying

def main():
    print("What is your name challenger?")
    name = input()
    hero = Hero(name, 50)

    dragons = [
        Dragon("Deadly Nadder", 10),
        Fire("Gronckle", 15),
        Flying("Timberjack", 20)
    ]
    
    print("Welcome to dragon training, " + hero.name)
    print("You must defeat 3 dragons.")

    while hero.hp > 0 and len(dragons) > 0:
        print(hero)
        for i in range(len(dragons)):
            print(str(i + 1) + ". Attack " + str(dragons[i]))

        dragon_choice = check_input.get_int_range("Choose a dragon to attack: ", 1, len(dragons))
        selected_dragon = dragons[dragon_choice - 1]

        print("Attack with:")
        print("1. Arrow (1 D12)")
        print("2. Sword (2 D6)")
        weapon_choice = check_input.get_int_range("Enter weapon ", 1, 2)

        if weapon_choice == 1:
            print(hero.arrow_attack(selected_dragon))
        else:
            print(hero.sword_attack(selected_dragon))

        if selected_dragon.hp <= 0:
            print("You defeated the " + selected_dragon.name + "!")
            dragons.remove(selected_dragon)

            if len(dragons) == 0:
                print("Congratulations! You have defeated all the dragons, you have passed the trial.")
                break

        attacking_dragon = random.choice(dragons)
        attack_type = random.randint(1, 2)

        if attack_type == 1:
            print(attacking_dragon.basic_attack(hero))
        else:
            print(attacking_dragon.special_attack(hero))

        if hero.hp <= 0:
            print("You have been defeated by the dragons.")
            print("You have failed the trial.")
            break
    
main()