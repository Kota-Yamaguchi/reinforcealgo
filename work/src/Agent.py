
from environment import Environment
from status import Status, Action
import random
import numpy as np
class Agent():
    def __init__(self, status: Status):
        self.status :Status = status
        self.next_status :Status = Status()

    @staticmethod
    def actions() -> list:
        return [Action.UP, Action.DOWN, Action.RIGHT, Action.LEFT]

    def move_by_policy(self)-> int:
        return random.choice(self.actions())

    def _one_step(self, action:int, environment: Environment) -> bool:
        probs :list = environment.transit_function(action)
        selected_action = np.random.choice(self.actions(), p = probs)
        print("agent select action : "+ str(selected_action))
        # ここ間違っている。next_stateを用意してそれでゴールかどうかの判定を実施してください
         #次に移動するマスの計算
        
        if (selected_action==Action.UP):
            self.next_status.row_position = self.status.row_position + 1
        if (selected_action==Action.DOWN):
            self.next_status.row_position = self.status.row_position + -1
        if selected_action==Action.RIGHT:
            self.next_status.column_position  = self.status.column_position + 1
        if selected_action==Action.LEFT:
            self.next_status.column_position  =  self.status.column_position + -1

        
        print("go next position "+str(self.next_status)+" ?")

        if environment.can_action_at(self.next_status):
            self.status.copy_status(self.next_status)
            print("go next position")
            return False
        else:
            if environment.is_goal(self.next_status):
                self.status.copy_status(self.next_status)
                print("reach goal")
                return True
            else:
                self.next_status.copy_status(self.status)
                print("can't go the direction")
        return False


    def start_by_goal(self, env: Environment) -> None:
        
        done : bool = False
        while not done:
            action = self.move_by_policy()
            
            done = self._one_step(action, env)
            env.calc_reward(self.status)
            
            print(self.status, env.reward)
        

        print("Complete")
        print("your reward is {}".format(env.reward))


            
