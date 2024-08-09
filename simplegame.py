#!/usr/bin/python3
"""
Simple Dungeon RPG: Quest for the Ancient Sword | John

A simplified RPG where the player chooses a class (Warrior or Mage),
navigates through a dungeon, fights demons, and searches for an ancient sword.
Driving a simple game framework with a dictionary object.
"""
import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.inventory = []

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def use_item(self, item):
        if item == "health potion":
            heal_amount = 20
            self.health = min(self.health + heal_amount, self.max_health)
            print(f"You used a health potion and gained {heal_amount} health!")
            return True
        return False

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=60, attack_power=15)
        self.shield_active = False

    def special_ability(self):
        if not self.shield_active:
            self.shield_active = True
            print("Warrior activates Shield Wall! Damage taken is reduced for the next attack.")

    def take_damage(self, damage):
        if self.shield_active:
            damage = max(1, damage // 2)
            print(f"Shield Wall absorbs half the damage! You take {damage} damage.")
            self.shield_active = False
        super().take_damage(damage)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=40, attack_power=10)
        self.mana = 100

    def special_ability(self):
        if self.mana >= 20:
            self.mana -= 20
            damage = random.randint(15, 25)
            print(f"Mage casts Fireball! Dealing {damage} damage.")
            return damage
        else:
            print("Not enough mana to cast Fireball.")
            return 0

    def attack(self):
        self.mana = min(self.mana + 10, 100)
        return super().attack()

rooms = {
    "Entrance": {"north": "Main Hall"},
    "Main Hall": {"north": "Throne Room", "east": "Armory", "south": "Entrance"},
    "Armory": {"west": "Main Hall"},
    "Throne Room": {"south": "Main Hall"}
}

room_items = {
    "Armory": ["health potion"],
    "Throne Room": ["ancient sword"]
}

demons = {
    "Main Hall": {"name": "Lesser Demon", "health": 20, "attack": 8},
    "Throne Room": {"name": "Demon Lord", "health": 30, "attack": 12}
}

def show_instructions():
    print("Simple Dungeon RPG: Quest for the Ancient Sword")
    print("Collect the Ancient Sword to win!")
    print("Commands: go [direction], get [item], use [item], fight, special, quit")

def show_status(current_room, player):
    print("\n-------------------------")
    print(f"You are in the {current_room}")
    print(f"Class: {player.__class__.__name__}")
    print(f"Health: {player.health}/{player.max_health}")
    if isinstance(player, Mage):
        print(f"Mana: {player.mana}/100")
    print(f"Inventory: {player.inventory}")
    print("-------------------------")

    if current_room in room_items and room_items[current_room]:
        print(f"You see: {', '.join(room_items[current_room])}")

    if current_room in demons:
        print(f"There's a {demons[current_room]['name']} here!")

def fight(player, demon):
    print(f"\nYou're fighting the {demon['name']}!")
    while player.health > 0 and demon['health'] > 0:
        action = input("Do you want to (a)ttack, use (s)pecial ability, or (r)un? ").lower()
        if action == 'a':
            player_damage = player.attack()
            demon['health'] -= player_damage
            print(f"You deal {player_damage} damage to the {demon['name']}.")
        elif action == 's':
            if isinstance(player, Warrior):
                player.special_ability()
            elif isinstance(player, Mage):
                demon['health'] -= player.special_ability()
        elif action == 'r':
            if random.random() < 0.5:
                print("You managed to escape!")
                return True
            else:
                print("You failed to escape.")
        else:
            print("Invalid action. Try again.")
            continue

        if demon['health'] <= 0:
            print(f"You defeated the {demon['name']}!")
            return True

        demon_damage = random.randint(1, demon['attack'])
        player.take_damage(demon_damage)
        print(f"The {demon['name']} deals {demon_damage} damage to you.")

    if player.health <= 0:
        print("You have been defeated...")
        return False

    return True

def main():
    print("Choose your class:")
    print("1. Warrior (Higher health, Shield Wall ability)")
    print("2. Mage (Lower health, Fireball ability)")

    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            player = Warrior("Warrior")
            break
        elif choice == "2":
            player = Mage("Mage")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    current_room = "Entrance"

    show_instructions()

    while True:
        show_status(current_room, player)

        move = input("What's your next move? ").lower().split()

        if move[0] == "go":
            if len(move) < 2:
                print("Go where?")
                continue
            direction = move[1]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")

        elif move[0] == "get":
            if len(move) < 2:
                print("Get what?")
                continue
            item = " ".join(move[1:])
            if current_room in room_items and item in room_items[current_room]:
                player.inventory.append(item)
                room_items[current_room].remove(item)
                print(f"You picked up {item}")
                if item == "ancient sword":
                    print("\nCongratulations! You found the Ancient Sword and won the game!")
                    break
            else:
                print("Can't get that item!")

        elif move[0] == "use":
            if len(move) < 2:
                print("Use what?")
                continue
            item = " ".join(move[1:])
            if item in player.inventory:
                if player.use_item(item):
                    player.inventory.remove(item)
                else:
                    print(f"You can't use {item} right now.")
            else:
                print(f"You don't have a {item}.")

        elif move[0] == "fight":
            if current_room in demons:
                if fight(player, demons[current_room]):
                    del demons[current_room]
                else:
                    print("Game Over!")
                    break
            else:
                print("There's nothing to fight here.")

        elif move[0] == "special":
            if current_room in demons:
                player.special_ability()
            else:
                print("There's no need to use your special ability right now.")

        elif move[0] == "quit":
            print("Thanks for playing!")
            break

        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
