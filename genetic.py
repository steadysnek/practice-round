import random
import util
from typing import NamedTuple, List
import problem

class Delivery(NamedTuple):
    team_size: int
    pizzas: List[int]  # list of pizza indexes

class Deliveries:
    def __init__(self):
        self.deliveries = []

    def random_init(self):
        used_pizza_indexes = []
        team_counts_left = problem.team_counts.copy()

        # Note: while stop condition is not currently correct, might infinite loop
        while len(used_pizza_indexes) < problem.num_pizzas:
            # choose random team size
            team_size = util.random_weighted_choice(problem.team_counts.items())

            # if enough pizzas are remaining
            if problem.num_pizzas - len(used_pizza_indexes) >= team_size:
                # choose n random remaining pizzas
                pizzas = []
                for i in range(team_size):
                    # pizza_i = random.randrange(0, len(pizzas))
                    pizza_i = random.choice(list(set(range(problem.num_pizzas)) - set(used_pizza_indexes)))
                    pizzas.append(pizza_i)
                    used_pizza_indexes.append(pizza_i)

                self.deliveries.append(Delivery(team_size, pizzas))
                team_counts_left[team_size] -= 1

    def format(self):
        print(len(self.deliveries))

        for delivery in self.deliveries:
            print(str(delivery.team_size) + " " + " ".join(map(str, delivery.pizzas)))

d = Deliveries()
d.random_init()
print(d)