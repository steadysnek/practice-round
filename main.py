pizzas = []  # index = pizza #, val = set of ingredients

with open("in.txt", "r") as f:
    line = map(int, f.readline().strip().split(" "))
    num_pizzas = next(line)
    team_sizes = tuple(line)

    for line in f:
        line = line.strip().split(" ")
        pizzas.append(set(line[1:]))

print(pizzas)