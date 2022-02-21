# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:25:58 2022

@author: ASUS
"""

probability = [0.99, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
reward = [1, 5, 10, 50, 100, 500, 1000, 5000, 15000, 30000]


class QuizProblem(object):

    def __init__(self, N):
        self.N = N

    def startState(self):
        return 1

    def isEnd(self, state):
        return state == self.N

    def actions(self, state):
        # list of actions
        result = []
        if state == 1:
            result.append('play')
            return result
        if state < self.N:
            result.append('quit')
            result.append('play')
        if state == self.N:
            result.append('none')
        return result

    # result[] -> list of (newState, probability, reward)
    # in our terms: newState = s', probability = T(s, a, s'), reward = R(s, a, s')
    # a = action, s = state

    def succProbReward(self, state, action):
        result = []
        # if the action == 'play', then -> newState = state+1,
        # probability = the probability to guess right and the reward for that action
        # or, if action == 'play', we can guess wrong and end up in the End state, with prob = 1-prob
        # and the reward of guessing wrong will be losing all reward he earned so far
        if action == 'play':
            result.append((state + 1, probability[state - 1], reward[state - 1]))
            result.append((self.N, 1 - probability[state - 1], -sum(reward[0:state - 1])))
        # if the action == 'quit', then -> newState = End state, with prob = 1,
        # reward = sum of all reward he reached so far
        elif action == 'quit':
            result.append((self.N, 1, sum(reward[0:state - 1])))
        return result

    def states(self):
        return range(1, self.N + 1)

    def discount(self):
        return 1


def valueIteration(mdp):
    # initialize all optimal values to 0, Vopt[state] = 0
    V = {}
    pi = {}
    for state in mdp.states():
        V[state] = 0

    # iterating all states and actions and return the sum according to the formula of Q-values
    # then, iterating using succProbReward func and result list
    # result[0] = the value of state->state+1, result[1] = transition probability = T(s, a, s'), result[2] = reward = R(s, a, s')
    def Q(state, action):
        return sum(result[1] * (result[2] + mdp.discount() * V[result[0]])
                   for result in mdp.succProbReward(state, action))

    # newV -> while iterating, computing the new values with Q-values by given the old values of V,
    # by given the old values of V, iterating until converge
    # newV it's the new max(Q-value)
    # pi[state] = result[1] for each newV that maximizes the value, we store the action the maximizes that value in pi
    while True:
        newV = {}
        for state in mdp.states():
            if mdp.isEnd(state):
                newV[state] = 0
                pi[state] = 'none'
            else:
                # the action that maximizes the Q-values
                result = max((Q(state, action), action) for action in mdp.actions(state))
                pi[state] = result[1]
                newV[state] = result[0]
        # checking for convergence
        if max(abs(V[state] - newV[state]) for state in mdp.states()) < 1e-3:
            break
        V = newV
        # print("\033[H\033[J")
        # print('{:>2} {:>10} {:>10}'.format('s','V(s)','pi'))
        # for state in mdp.states():
        # print('{:>2} {:>10.2f} {:>11}'.format(state,V[state],pi[state]))
        # input()
    return pi


if __name__ == '__main__':
    mdp = QuizProblem(N=11)
    valueIteration(mdp)

