
from status import Status, Action
import random
import numpy as np
class Agent():
    def __init__(self, state: Status):
        self.state :Status = state
        self.next_state :Status = Status()
        self.pi_dict1 = {Action.UP:0.25, Action.DOWN:0.25,Action.RIGHT:0.25, Action.LEFT:0.25} 

    @staticmethod
    def actions() -> list:
        return [Action.UP, Action.DOWN, Action.RIGHT, Action.LEFT]

    def move_by_policy(self)-> int:
        return random.choice(self.actions())

    def pi(self, action):
        return self.pi_dict1[action]

            
