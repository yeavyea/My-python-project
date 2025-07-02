def animal_sounds(animals):
    for animal in animals:
        if animal == "cat":
            print("cat → meow")
        elif animal == "dog":
            print("dog → ruff")
        elif animal == "cow":
            print("cow → moo")
        elif animal == "duck":
            print("duck → guack")
        else:
            print(f"{animal} → unknown sound")
            
my_animals = ["cat","dog","cow","duck","fish"]

print(animal_sounds)
            
