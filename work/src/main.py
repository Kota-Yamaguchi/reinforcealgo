from Agent import Agent
from environment import Environment
from status import Status, Action




def main():
    grid = [
        [0, 0, 0, 1],
        [0, 9, 0, -1],
        [0, 0, 0, 0]
    ]
    status : Status = Status()
    agent :Agent = Agent(status)
    env : Environment = Environment(grid, 0.8)

    agent.start_by_goal(env)



main()