import math
import os
from abc import ABC, abstractmethod


class BaseDataSet(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

        with open(file_path, "r") as fh:
            self.parse(fh)

    @abstractmethod
    def parse(self, fh):
        pass

    def output(self, text):
        os.makedirs("out", exist_ok=True)
        out_file_path = os.path.join("out", os.path.basename(self.file_path))

        with open(out_file_path, "w") as fh:
            fh.write(text)

# noinspection PyAttributeOutsideInit


class DataSet(BaseDataSet):
    def parse(self, fh):
        self.pizzas = []  # index = pizza #, val = set of ingredients
        line = map(int, fh.readline().strip().split(" "))
        self.num_pizzas = next(line)
        self.team_counts = {i + 2: count for i,
                            count in enumerate(line)}  # {team size : count}

        for line in fh:
            line = line.strip().split(" ")
            self.pizzas.append(set(line[1:]))


class UnoDataSet(BaseDataSet):
    def parse(self, fh):
        split_file = [line.split() for line in fh.read().splitlines()]
        meta_data = split_file[0]
        self.num_pizzas = meta_data[0]
        self.team_counts = meta_data[1:]

        ingredients = {}
        self.pizzas = {}

        ingredient_count = 0
        for line in split_file[1:]:
            amount = int(line[0])
            bit_counter = 0
            for ingredient in line[1:]:
                if(ingredient not in ingredients):
                    ingredients[ingredient] = ingredient_count
                    ingredient_count += 1
                bit_counter += 1 << ingredients[ingredient]

            self.pizzas[bit_counter] = self.pizzas.get(bit_counter, 0) + amount
