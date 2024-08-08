farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
def part1():
    for farm in farms:
        if farm["name"] == "NE Farm":
            for animal in farm["agriculture"]:
                print(animal)
    print()

def part2():
    farm_choice = input("choose a farm(NE Farm, W Farm, or SE Farm):")
    for farm in farms:
        if farm ["name"] == farm_choice:
            print(f"Plants/animals on {farm_choice}: {farm['agriculture']}")
            break
    print()

def part3():
    farm_choice = input(" Choose a farm (NE Farm, W Farm, W Farm, or SE Farm): ")
    print(f"Animals on {farm_choice}:")
    for farm in farms:
        if farm["name"] == farm_choice:
            for item in farm["agriculture"]:
                if not item in ["carrots", "celery"]:
                    print(item)
                break
    print()

def main():
    part1()
    part2()
    part3()
if __name__=="__main__":
    main()
