import numpy as np
class Node:
    def __init__(self,size:int,data_type):
        self.size = size
        self.type = data_type
        self.cachy_node=np.empty(self.size,dtype=self.data_type)
