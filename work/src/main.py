from Agent import Agent
from environment import Environment
from status import Status, Action
import matplotlib.pyplot as plt



def main():
    grid = [[0,0,10,0,0],
            [0,0,0,0,10],
            [0,0,10,0,0],
            [0,0,0,0,0],
            [0,0,0,20,0,]]
    status : Status = Status()
    agent :Agent = Agent(status)
    env : Environment = Environment(grid, agent, 0.8)

    value_array = env.calc_iterative_state_value()

    fig, ax = plt.subplots()
    heatmap = ax.pcolor(value_array, cmap=plt.cm.Blues)
    plt.show()


main()