from wild_cat_zoo.animal import Animal
from wild_cat_zoo.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal: Animal, price: int):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget < price:
                return "Not enough budget"
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        else:
            return "Not enough space for animals"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.owner == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_for_pay= 0
        for worker in self.workers:
            sum_for_pay += worker.salary

        if self.__budget >= sum_for_pay:
            self.__budget -= sum_for_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_care = 0
        for animal in self.animals:
            money_for_care += animal.money_for_care

        if self.__budget >= money_for_care:
            self.__budget -= money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        animals_types = {"Lion": [],
                         "Tiger": [],
                         "Cheetah": []
                         }
        result = f"You have {len(self.animals)} animals\n"
        for aniamal in self.animals:
            animals_types[aniamal.__class__.__name__].append(aniamal)
        for aniamal, animals in animals_types.items():
            result += f"----- {len(animals)} {aniamal + 's'}:\n"
            for a in animals:
                result += a.__repr__() + '\n'
        return result.strip()

    def workers_status(self):
        workers_types = {"Keeper": [],
                         "Caretaker": [],
                         "Vet": []
                         }
        result = f"You have {len(self.workers)} workers\n"
        for worker in self.workers:
            workers_types[worker.__class__.__name__].append(worker)
        for worker, workers in workers_types.items():
            result += f"----- {len(workers)} {worker + 's'}:\n"
            for w in workers:
                result += w.__repr__() + '\n'
        return result.strip()