import random
import util
from typing import NamedTuple, List
from problem import DataSet
data_set = DataSet("res/d.txt")

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
        used_pizza_indexes = set()
        team_counts_left = data_set.team_counts.copy()

        for delivery in self.deliveries:
            team_counts_left[delivery.team_size] -= 1
            used_pizza_indexes.update(delivery.pizzas)

        # drop empty team_sizes from consideration
        team_counts_left = {k:v for k, v in team_counts_left.items() if v > 0}

        while True:
            # choose random team size
            team_size = util.random_weighted_choice(team_counts_left.items())

            # if enough pizzas are remaining
            if data_set.num_pizzas - len(used_pizza_indexes) >= team_size:
                # choose n random remaining pizzas
                pizzas = []
                for i in range(team_size):
                    # pizza_i = random.randrange(0, len(pizzas))
                    pizza_i = random.choice(list(set(range(data_set.num_pizzas)) - used_pizza_indexes))
                    pizzas.append(pizza_i)
                    used_pizza_indexes.add(pizza_i)

                self.deliveries.append(Delivery(team_size, pizzas))

                team_counts_left[team_size] -= 1
                if team_counts_left[team_size] <= 0:
                    team_counts_left.pop(team_size)

            smallest_remaining_team_size = min(team_counts_left.keys())
            remaining_pizza_count = data_set.num_pizzas - len(used_pizza_indexes)
            if remaining_pizza_count < smallest_remaining_team_size:
                break

    def format(self):
        ret = str(len(self.deliveries)) + "\n"

        for delivery in self.deliveries:
            ret += str(delivery.team_size) + " " + " ".join(map(str, delivery.pizzas)) + "\n"
        return ret

d = Deliveries()
d.random_assign()
print(d.format())
data_set.output(d.format())