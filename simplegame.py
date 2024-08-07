"""
Simple Dungeon RPG: Quest for the Ancient Sword
Author: John

A simplified RPG where the player navigates through a dungeon,
fights demons, and searches for an ancient sword.
"""

import random

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
    "Main Hall": {"name": "Lesser Demon", "health": 20},
    "Throne Room": {"name": "Demon Lord", "health": 30}
}

def show_instructions():
    print("Simple Dungeon RPG: Quest for the Ancient Sword")
    print("Collect the Ancient Sword to win!")
    print("Commands: go [direction], get [item], use [item], fight, quit")

def show_status(current_room, inventory, health):
    print("\n-------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    print(f"Health: {health}")
    print("-------------------------")
    
    if current_room in room_items and room_items[current_room]:
        print(f"You see: {', '.join(room_items[current_room])}")
    
    if current_room in demons:
        print(f"There's a {demons[current_room]['name']} here!")

def fight(player_health, demon):
    print(f"\nYou're fighting the {demon['name']}!")
    while player_health > 0 and demon['health'] > 0:
        action = input("Do you want to (a)ttack or (r)un? ").lower()
        if action == 'a':
            player_damage = random.randint(5, 15)
            demon['health'] -= player_damage
            print(f"You deal {player_damage} damage to the {demon['name']}.")
            if demon['health'] <= 0:
                print(f"You defeated the {demon['name']}!")
                return player_health
            
            demon_damage = random.randint(3, 10)
            player_health -= demon_damage
            print(f"The {demon['name']} deals {demon_damage} damage to you.")
        elif action == 'r':
            if random.random() < 0.5:
                print("You managed to escape!")
                return player_health
            else:
                print("You failed to escape.")
                demon_damage = random.randint(3, 10)
                player_health -= demon_damage
                print(f"The {demon['name']} deals {demon_damage} damage to you.")
        else:
            print("Invalid action. Try again.")
    
    if player_health <= 0:
        print("You have been defeated...")
    
    return player_health

def main():
    current_room = "Entrance"
    inventory = []
    health = 50
    
    show_instructions()
    
    while True:
        show_status(current_room, inventory, health)
        
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
                inventory.append(item)
                room_items[current_room].remove(item)
                print(f"You picked up {item}")
                if item == "Ancient Sword":
                    print("\nCongratulations! You found the Ancient Sword and won the game!")
                    break
            else:
                print("Can't get that item!")

        elif move[0] == "use":
            if len(move) < 2:
                print("Use what?")
                continue
            item = " ".join(move[1:])
            if item in inventory:
                if item == "Health Potion":
                    health += 20
                    inventory.remove(item)
                    print("You used the Health Potion and gained 20 health!")
                else:
                    print(f"You can't use {item} right now.")
            else:
                print(f"You don't have a {item}.")
        
        elif move[0] == "fight":
            if current_room in demons:
                health = fight(health, demons[current_room])
                if health <= 0:
                    print("Game Over!")
                    break
                del demons[current_room]
            else:
                print("There's nothing to fight here.")
        
        elif move[0] == "quit":
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()

