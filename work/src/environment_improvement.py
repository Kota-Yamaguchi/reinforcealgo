
from turtle import done
from status import Status, Action
import numpy as np
from Agent import Agent 

class EnvironmentImpl():
    def __init__(self, grid : list, agent : Agent, move_prob =0.8):
        self.default_rewarding = -0.04
        self.grid = grid
        self.row = len(grid)
        self.column = len(grid[0])
        self.move_prob = 0.8
        self.agent : Agent = agent

    def can_action_at(self, state: Status) -> bool:
        #マス目の端からはとびだせない
        if state.column_position <0:
            return False
        if state.row_position  <0:
            return False
        if state.column_position > self.column-1:
            return False
        if state.row_position > self.row -1:
            return False
        #何かの報酬があるマスの時に動けない
        if self.grid[state.row_position][state.column_position] == 9:
            return False
        

        return True

    def is_goal(self, state : Status) -> bool:
        #マス目の端からはとびだせない
        if state.column_position <0:
            return False
        if state.row_position  <0:
            return False
        if state.column_position > self.column-1:
            return False
        if state.row_position > self.row -1:
            return False

        value :int = self.grid[state.row_position][state.column_position]
        print("is goal ?")
        if value == 10:
            return True
        elif value == 20:
            return True
        return False

    # policyで選ばれた後に環境で動きが左右される。
    def transit_function(self, action) -> list:
        probs = []
        oposite_direction = Action(action.value *-1)
      
        actions = self.agent.actions()
        for a in actions:
            
            if a == action:
                
                probs.append(self.move_prob)
                
            elif a != oposite_direction:
                probs.append( (1-self.move_prob)/2 )
               
            else:
                probs.append(0)
        
        return probs

    def move_next_state(self, action:int, state :Status) -> Status:
        
        selected_action = action
        # print("agent select action : "+ str(selected_action))
        next_state :Status = Status()
        if (selected_action==Action.UP):
            next_state.row_position = state.row_position + 1
            next_state.column_position  = state.column_position
        if (selected_action==Action.DOWN):
            next_state.row_position = state.row_position + -1
            next_state.column_position  = state.column_position
        if selected_action==Action.RIGHT:
            next_state.row_position = state.row_position
            next_state.column_position  = state.column_position + 1

        if selected_action==Action.LEFT:
            next_state.row_position = state.row_position
            next_state.column_position  =  state.column_position + -1

        return next_state

    def _one_step(self, action:int) -> bool:
        
        # ここ間違っている。next_stateを用意してそれでゴールかどうかの判定を実施してください
         #次に移動するマスの計算
        
        self.agent.next_state  = self.move_next_state(action, self.agent.state)
        # print("go next position "+str(self.agent.next_state)+" ?")

        if self.can_action_at(self.agent.next_state):
            self.agent.state.copy_status(self.agent.next_state)
            # print("go next position")
            if self.is_goal(self.agent.state):
                print("reach goal")
                return True

            return False
        else:
            self.agent.next_status.copy_status(self.agent.state)
            # print("can't go the direction")
        return False

    def iterative_policy(self):
        pi = np.random.randint(0, len(self.agent.actions()), (self.row, self.column))
        value_grid = np.zeros((len(self.grid), len(self.grid[0])))
        is_policy_stable : bool = False
        while not is_policy_stable:
        
            value_grid = self.calc_iterative_state_value(value_grid, pi)
            is_policy_stable = self.calc_policy_improvement(value_grid, pi)

        return pi, value_grid

    def calc_iterative_state_value(self,value_grid, pi, gamma : float = 0.9):
        count = 0
        
        actions = self.agent.actions()
        while(True):
            delta = 0
            for i in range(len(self.grid)):
                for j in range(len(self.grid[0])):
                    tmp = 0
                    tmp_v = value_grid[i][j]
                    action = actions[pi[i][j]]
                    self.agent.state.set_status(i, j)
                    next_state : Status= self.move_next_state(action, self.agent.state)
                    
                    done = self.can_action_at(next_state)
                    if not done:
                        tmp += self.calc_reward(next_state)
                        continue
                    else:
                        reward : float = self.calc_reward(next_state)
                        V_pi = gamma * value_grid[next_state.row_position][next_state.column_position] 
                        tmp = (reward + V_pi )
                    value_grid[i][j] = tmp
                    delta = max(delta , abs(tmp_v - value_grid[i][j]))
            count +=1
            print("count: %d, delta: %f, abs: %f" % (count, delta, abs(tmp_v-value_grid[i,j])))
            if delta < 0.1:
                break
        return value_grid

    def calc_policy_improvement(self, value_grid,pi, gamma : float = 0.9) ->bool :
        actions = self.agent.actions()
        b = pi.copy()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                tmp = np.zeros(len(actions))
                for index, action in enumerate(actions):
                    self.agent.state.set_status(i, j)
                    next_state : Status= self.move_next_state(action, self.agent.state)
                    reward : float = self.calc_reward(next_state)
                    done = self.can_action_at(next_state)
                    if not done:
                        tmp +=  self.calc_reward(next_state)
                        continue
                    V_pi = gamma * value_grid[next_state.row_position][next_state.column_position] 
                    tmp[index] = (reward + V_pi )
                pi[i, j] = np.argmax(tmp)
        if (np.all(b == pi)):
            print("policy stable")
            return True
        return False
        


    def calc_recursive_state_value(self):
        now_num : int = 0
        iter_num :int = 6
        out : float = 0
        done: bool = False

        value_grid = np.zeros((len(self.grid), len(self.grid[0])))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.agent.state.set_status(i, j)
                value_grid[i][j] = self.V_pi(now_num, iter_num, self.agent.state, out)
                # value_grid[i][j] = self.V_pi_by_goal(done, self.agent.state, out)
                print(value_grid[i][j])
        return value_grid

    def calc_reward(self, state:Status) -> float:
        
        if not self.can_action_at(state):
            return -1
        
        if self.grid[state.row_position][state.column_position] ==0:
            return self.default_rewarding
        else:
            return self.grid[state.row_position][state.column_position]
        # 再帰では動かせない例として表示
    def V_pi_by_goal(self, done:bool, state: Status, out : float ) ->float:
        gamma : float = 0.9

        actions =self.agent.actions()
        if (done):
            out = out + self.calc_reward(state)
            return out
        else:
            for action in actions:
                probs = self.transit_function(action)
                for p in probs:
                    next_state : Status= self.move_next_state(action, state)
                    reward : float = self.calc_reward(next_state)
                    done = self.can_action_at(next_state) or self.is_goal(next_state)
                    next_state = next_state if done else state
                    out += self.agent.pi(action) * p * (reward + gamma* self.V_pi_by_goal(done, next_state, out) )
            return out

    #　再帰でなんとか動かすための例　ほとんど計算できひんし、収束しない 
    def V_pi(self, now_num: int, iter_num : int,  state: Status, out : float ) ->float:
        gamma : float = 0.6
        actions =self.agent.actions()
        if iter_num == now_num:
            for action in actions:
                out +=  self.agent.pi(action) * self.calc_reward(state)
            return out
        else:
            now_num += 1
            for action in actions:
                # probs = self.transit_function(action)
                # for p in probs:
                next_state : Status= self.move_next_state(action, state)
                reward : float = self.calc_reward(next_state)
                done = self.can_action_at(next_state)
                if not done:
                    out +=  self.agent.pi(action) * self.calc_reward(state)
                    continue
                next_state = next_state if done else state
                # out += self.agent.pi(action) * p * (reward + gamma* self.V_pi(now_num, iter_num, next_state, out) )
                pi = self.agent.pi(action)
                V_pi = gamma* self.V_pi(now_num, iter_num, next_state, out)
                out += pi *(reward + V_pi )
            
            return out