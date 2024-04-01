from gym.customer import Customer
from gym.equipment import Equipment
from gym.exercise_plan import ExercisePlan
from gym.subscription import Subscription
from gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = list()
        self.trainers = list()
        self.equipment = list()
        self.plans = list()
        self.subscriptions = list()

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = None
        for s in self.subscriptions:
            if s.id == subscription_id:
                subscription = s
        result = ""
        if subscription:
            result += str(subscription)

            for c in self.customers:
                if c.id == subscription.customer_id:
                    result += '\n' + str(c)

            for t in self.trainers:
                if t.id == subscription.trainer_id:
                    result += '\n' + str(t)

            for e in self.equipment:
                if e.id == subscription_id:
                    result += '\n' + str(e)

            for p in self.plans:
                if p.id == subscription_id:
                    result += '\n' + str(p)

        return result
