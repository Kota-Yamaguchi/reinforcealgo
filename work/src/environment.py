
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

    def can_action_at(self, action: int, status: Status) -> bool:
        
        #何かの報酬があるマスの時に動けない
        if self.grid[status.row_position][status.column_position] != 0:
            return False
        
        #次に移動するマスの計算
        next_row : int = 0
        next_column : int = 0
        
        if (action==Action.UP):
            next_row = status.row_position + 1
        if (action==Action.DOWN):
            next_row = status.row_position + -1

        if action==Action.RIGHT:
            next_column = status.column_position + 1
        if action==Action.LEFT:
            next_column =  status.column_position + -1

        #マス目の端からはとびだせない
        if next_column <0:
            return False
        if next_row  <0:
            return False
        if next_column > self.column:
            return False
        if next_row > self.row :
            return False

        return True

    def is_goal(self, status : Status) -> bool:
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
        print(probs)
        return probs

    def calc_reward(self, status:Status) -> float:
        
        if self.grid[status.row_position][status.column_position] ==0:
            self.reward += self.default_rewarding
        else:
            self.reward += self.grid[status.row_position][status.column_position]
        return self.reward