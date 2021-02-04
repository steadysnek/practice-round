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

    def random_assign(self):
        """
        Randomly assign any remaining valid deliveries
        :return:
        """
        used_pizza_indexes = []
        team_counts_left = problem.team_counts.copy()

        while True:
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

            smallest_remaining_team_size = min(team_counts_left.keys())
            remaining_pizza_count = problem.num_pizzas - len(used_pizza_indexes)
            if remaining_pizza_count <= smallest_remaining_team_size:
                break

    def format(self):
        print(len(self.deliveries))

        for delivery in self.deliveries:
            print(str(delivery.team_size) + " " + " ".join(map(str, delivery.pizzas)))

d = Deliveries()
d.random_assign()
print(d)