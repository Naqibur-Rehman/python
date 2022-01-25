from data import plants_dict, plants_list, people

# people = []

if bool(people) and all([person[1] for person in people]):
    print("sending email")
else:
    print("user must edit the recipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grass in this pack")

if any(plants_dict[key].plant_type == "Grass" for key in plants_dict):
    print("This pack contains grass")
else:
    print("No grass in this pack")

if any(plant.plant_type == "Grass" for plant in plants_dict.values()):
    print("This pack contains grass")
else:
    print("No grass in this pack")

if any(plants_dict[key].plant_type == "Cactus" for key in plants_dict):
    print("This pack contains grass")
else:
    print("No grass in this pack")
