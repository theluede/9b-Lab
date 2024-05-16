# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:22:13 2024

@author: klued
"""

params = {'world_size':(20,20),
          'num_agents':380}

class Agent():
    def __init__(self): ## start up parameters
        pass
    def move(self):
        ## makes the agent move
        pass
## creates foundation to be able to add complexity    
class World():
    def __init__(self):
        self.grid = self.build_grid(params['world_size'])
        self.agents = self.build_agents(params['num_agents'])
        
    def build_grid(self, world_size):
    ##create the world that the agents can move around on
        locations = [(i,j) for i in range(world_size[0]) for j in range(world_size[1])]
        return {l:None for l in locations}
    def build_agents(self, num_agents):
        agents = [Agent() for i in range(num_agents)] ## i'm calling the agent class here
        return agents
    def report_integration(self):
        ## generates a report, don't know what type of report we want
        pass
    def report (self):
        pass

one = Agent() ## the self in agent will be referenced in one
two = World() ## the self in world will be referenced in two
