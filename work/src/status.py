from enum import Enum
import numpy as np

class Action(Enum):
    UP = 1
    DOWN = -1
    RIGHT = 2
    LEFT =-2

class Status():
    def __init__(self):
        

        self.row_position = 0
        self.column_position =0
    
    
    def update_status(self, action) -> None:
        if (action==Action.UP):
            self.row_position += 1
        if (action==Action.DOWN):
            self.row_position += -1

        if action==Action.RIGHT :
            self.column_position += 1
        if action==Action.LEFT:
            self.column_position += -1
        

    def set_column_position(self, column_position):
        self.column_position = column_position
        
    def set_row_position(self, row_position):
        self.row_position = row_position

    def __str__(self):
        return "your position :"+ str(self.row_position)+","+str(self.column_position) 



