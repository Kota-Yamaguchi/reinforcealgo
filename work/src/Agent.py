
from environment import Environment
from status import Status, Action
import random
import numpy as np
class Agent():
    def __init__(self, status: Status):
        self.status = status
    

    @staticmethod
    def actions() -> list:
        return [Action.UP, Action.DOWN, Action.RIGHT, Action.LEFT]

    def move_by_policy(self)-> int:
        return random.choice(self.actions())

    def _one_step(self, action:int, environment: Environment) -> bool:
        probs :list = environment.transit_function(action)
        selected_action = np.random.choice(self.actions(), p = probs)

        # ここ間違っている。next_stateを用意してそれでゴールかどうかの判定を実施してください

        if environment.can_action_at(action, self.status):
            self.status.update_status(selected_action)
            return False
        else:
            if environment.is_goal(self.status):
                
                print("reach goal")
                return True
            
        return False


    def start_by_goal(self, env: Environment) -> None:
        
        done : bool = False
        while not done:
            action = self.move_by_policy()
            print("agent select action : "+ str(action))
            print(done)
            done = self._one_step(action, env)
            env.calc_reward(self.status)
            
            print(self.status, done)
        

        print("Complete")



            
