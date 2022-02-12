from mlcs import *
import numpy as np


class Environment:
    def __init__(self, data_file):
        self.mlcs = MLCS.load_from_file(data_file)
        self.max_level = 0
        self.levels = []

    def reset(self):
        self.current_location = self.mlcs.next_locations(self.mlcs.start)
        self.current_level = 1
        next_location = [loc.index for loc in self.current_location]
        next_state = (np.array(next_location) / np.array(self.mlcs.seqs_len)).reshape(1, -1)
        self.reward = 0
        return next_state

    def step(self, action):
        done = False
        if self.current_location[action:]:
            self.current_location = self.current_location[action]
            current_reward = self.current_level  / np.max(np.array(self.current_location.index)) 
            reward = current_reward - self.reward
            self.reward = current_reward
            self.current_location = self.mlcs.next_locations(self.current_location)
            if self.current_location:
                self.current_level += 1
                next_location = [loc.index for loc in self.current_location]
                next_state = (np.array(next_location) / np.array(self.mlcs.seqs_len)).reshape(1, -1)
                if len(self.current_location) < len(self.mlcs.charset):
                    padding = np.zeros((1, len(self.mlcs.seqs) * (len(self.mlcs.charset) - len(self.current_location))))
                    next_state = np.concatenate((next_state, padding), axis=1)
            else:
                self.max_level = max(self.max_level, self.current_level)
                print('max level reached: {} !!!'.format(self.current_level))
                self.levels.append(self.current_level)
                done = True
                next_state = np.ones((1, len(self.mlcs.seqs) * len(self.mlcs.charset)))
        else:
            next_state = np.zeros((1, len(self.mlcs.seqs) * len(self.mlcs.charset)))
            done = True
            reward = 0

        return next_state, reward, done


