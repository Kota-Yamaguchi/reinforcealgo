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
    
    
    def set_status(self, row, column) -> None:
        self.row_position = row
        self.column_position = column
    

    def copy_status(self, status : "Status"):
        self.column_position = status.column_position
        self.row_position = status.row_position
        
    def __str__(self):
        return "your position :"+ str(self.row_position)+","+str(self.column_position) 



