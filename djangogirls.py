waiting_list = [
    "Laura",
    "Susanne",
    "Karolin",
    "Lisa",
    "Andrea",
    "Sabrine"
]

def print_position_in_waiting_list(name):
    position = 1
    for girl_name in waiting_list:
        if girl_name == name:
            print("Deine Position ist " + str(position))
        position = position + 1

print_position_in_waiting_list("Lisa")
print_position_in_waiting_list("Karolin")
