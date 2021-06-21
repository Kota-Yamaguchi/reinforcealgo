
from status import Status, Action
import numpy as np


class Environment():
    def __init__(self, grid : list, move_prob =0.8):
        self.default_rewarding = -0.04
        self.grid = grid
        self.row = len(grid)
        self.column = len(grid[0])
        self.reward = 0
        self.move_prob = 0.8

    def can_action_at(self, status: Status) -> bool:
        #マス目の端からはとびだせない
        if status.column_position <0:
            return False
        if status.row_position  <0:
            return False
        if status.column_position > self.column-1:
            return False
        if status.row_position > self.row -1:
            return False
        #何かの報酬があるマスの時に動けない
        if self.grid[status.row_position][status.column_position] != 0:
            return False
        

        return True

    def is_goal(self, status : Status) -> bool:
        #マス目の端からはとびだせない
        if status.column_position <0:
            return False
        if status.row_position  <0:
            return False
        if status.column_position > self.column-1:
            return False
        if status.row_position > self.row -1:
            return False

        value :int = self.grid[status.row_position][status.column_position]
        print("is goal ?")
        if value == 1:
            return True
        elif value == -1:
            return True
        return False

    # policyで選ばれた後に環境で動きが左右される。
    def transit_function(self, action) -> list:
        probs = []
        oposite_direction = Action(action.value *-1)
        from Agent import Agent
        actions = Agent.actions()
        for a in actions:
            
            if a == action:
                
                probs.append(self.move_prob)
                
            elif a != oposite_direction:
                probs.append( (1-self.move_prob)/2 )
               
            else:
                probs.append(0)
        
        return probs

    def calc_reward(self, status:Status) -> float:
        
        if self.grid[status.row_position][status.column_position] ==0:
            self.reward += self.default_rewarding
        else:
            self.reward += self.grid[status.row_position][status.column_position]
        return self.reward